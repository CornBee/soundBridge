from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse
from google.oauth2 import id_token
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport import requests as google_requests
from sqlalchemy.orm import Session
from config import GOOGLE_CLIENT_ID, REDIRECT_URI, GOOGLE_CLIENT_SECRET
from database import get_db
from models import User, InvitedEmail, InviteHistory
import os
from typing import List

router = APIRouter()

# Google Oauth2 설정 값을 환경변수로부터 불러옵니다.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

config = {
    "web": {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uris": [REDIRECT_URI],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
    }
}

flow = InstalledAppFlow.from_client_config(
    config,
    scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"]
)


@router.get("/login")
async def login(request: Request):
    flow.redirect_uri = REDIRECT_URI
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        prompt='consent',
        include_granted_scopes='true'
    )
    response = RedirectResponse(authorization_url)
    response.set_cookie("oauth_state", state, max_age=3600,
                        httponly=True)  # state 값을 쿠키에 저장, 1시간 뒤에 쿠키 만료
    return response


@router.get("/login/callback")
async def callback(request: Request, state: str = "", code: str = "", db: Session = Depends(get_db)):
    # 쿠키에서 state 값을 가져옴
    expected_state = request.cookies.get("oauth_state")

    if not expected_state:
        raise HTTPException(status_code=400, detail="State cookie is missing.")
    if state != expected_state:
        raise HTTPException(status_code=400, detail="MismatchingStateError")

    flow.fetch_token(code=code)

    credentials = flow.credentials
    token_info = id_token.verify_oauth2_token(
        credentials.id_token, google_requests.Request(), GOOGLE_CLIENT_ID
    )

    existing_user = db.query(User).filter(
        User.email == token_info["email"]).first()

    # 이미 가입된 사용자인 경우
    if existing_user and existing_user.username:
        return {"message": "Successfully logged in!", "redirect": "profile_page_url"}

    # 가입되지 않은 사용자인 경우
    invited_users = get_users_by_invited_email(token_info["email"], db)
    if not invited_users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not invited account")

    # 가입 페이지로 리디렉션
    return {"message": "Please complete registration", "redirect": "signup_page_url"}


def delete_invited_email(email: str, db: Session = Depends(get_db)):
    """
    데이터베이스에서 주어진 이메일 주소를 invited_emails 테이블에서 삭제합니다.
    """
    db.query(InvitedEmail).filter(InvitedEmail.invitee_email == email).delete()
    db.commit()


def create_new_user(email: str, name: str, inviter_id: int, db: Session = Depends(get_db)):
    # Create a new user
    new_user = User(email=email, name=name, invited_by=inviter_id)
    db.add(new_user)
    db.commit()

    # Add an entry to the invite_history table
    create_new_invite_history(inviter_id, new_user.user_id)

    # Remove the invite from the invited_emails table
    delete_invited_email(db, email)


def create_new_invite_history(inviter_id: int, invitee_id: int, db: Session = Depends(get_db)):
    """
    Adds a new invite history record to the database.
    """
    history = InviteHistory(inviter_id=inviter_id, invitee_id=invitee_id)
    db.add(history)
    db.commit()


def get_users_by_invited_email(email: str, db: Session) -> List[InvitedEmail]:
    """
    데이터베이스에서 주어진 이메일 주소와 일치하는 초대된 사용자 목록을 반환합니다.
    """
    return db.query(InvitedEmail).filter(InvitedEmail.invitee_email == email).all()
