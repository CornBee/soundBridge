from fastapi import APIRouter, HTTPException, Request, status, Depends
from fastapi.responses import RedirectResponse
from google.oauth2 import id_token
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport import requests as google_requests
from sqlalchemy.orm import Session
from config import GOOGLE_CLIENT_ID, REDIRECT_URI, GOOGLE_CLIENT_SECRET, GOOGLE_TOKEN_URI, GOOGLE_AUTH_URI
from database import get_db
from models import User, InvitedEmail, InviteHistory, UserCreate, SNSLink
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
        "auth_uri": GOOGLE_AUTH_URI,
        "token_uri": GOOGLE_TOKEN_URI,
    }
}

flow = InstalledAppFlow.from_client_config(
    config,
    scopes=["openid", "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile"]
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
        return RedirectResponse(url="/profile")

    # 초대되지 않은 사용자인 경우
    invited_users = get_users_by_invited_email(token_info["email"], db)
    if not invited_users:
        return RedirectResponse(url="/not_invited")

    # 초대된 사용자 정보를 기반으로 새로운 사용자를 생성합니다.
    invited_by = invited_users[0].invited_by  # 초대한 사람의 ID
    create_new_user(
        email=token_info["email"], name=token_info["name"], inviter_id=invited_by, db=db)

    return RedirectResponse(url="/signup?email=" + token_info["email"])


def delete_invited_email(email: str, db: Session = Depends(get_db)):
    """
    데이터베이스에서 주어진 이메일 주소를 invited_emails 테이블에서 삭제합니다.
    """
    db.query(InvitedEmail).filter(InvitedEmail.invitee_email == email).delete()
    db.commit()


def create_new_user(email: str, name: str, inviter_id: int, db: Session = Depends(get_db)):
    # Create a new user
    new_user = User(email=email, username=name, invited_by=inviter_id)
    db.add(new_user)
    db.commit()

    # Add an entry to the invite_history table
    create_new_invite_history(inviter_id, new_user.user_id, db)

    # Remove the invite from the invited_emails table
    delete_invited_email(email, db)


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

@router.get("/not_invited")
def not_invited():
    return {"message": "초대를 받지 않았습니다. 동료 뮤지션에게 초대 요청을 보내주세요."}


@router.post("/create_user")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # User 생성
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        profile_picture=user_data.profile_picture,
        one_line_intro=user_data.one_line_intro
    )
    db.add(new_user)
    db.commit()

    # SNS 링크들 생성
    for link in user_data.sns_links:
        sns_link = SNSLink(
            user_id=new_user.user_id,
            platform=link.platform,
            link_url=link.link_url
        )
        db.add(sns_link)
    db.commit()

    return {"message": "회원가입이 완료되었습니다."}