from fastapi import APIRouter, HTTPException, Request
from authlib.integrations.starlette_client import OAuth
from initialize_db import session
from models import User
from typing import Optional, Tuple
import json

router = APIRouter()

with open("OAuth_20.json", "r") as file:
    OAuth_20 = json.load(file)

# OAuth 설정
oauth = OAuth()
CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth.register(
    name="google",
    client_id=OAuth_20["web"]["client_id"],
    client_secret=OAuth_20["web"]["client_secret"],
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    access_token_url="https://accounts.google.com/o/oauth2/token",
    refresh_token_url=None,
    redirect_uri="http://localhost:8000/login/callback",
    client_kwargs={"scope": "openid profile email"},
)


@router.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/login/callback")
async def callback(request: Request, invite_code: str):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)

    # 여기서 user 정보와 invite_code를 사용하여 사용자 가입 로직을 처리합니다.

    # 예시:
    if is_valid_invite_code(invite_code):
        create_new_user(user["email"], user["name"], invite_code)
        return {"message": "Successfully registered with Google and invite code"}
    else:
        raise HTTPException(status_code=400, detail="Invalid invite code")


def get_user_by_invite_code(db: session, invite_code: str) -> Optional[User]:
    """
    데이터베이스에서 주어진 초대 코드에 해당하는 사용자를 반환합니다.
    만약 해당 사용자를 찾을 수 없다면 None을 반환합니다.
    """
    return db.query(User).filter(User.invite_code == invite_code).first()


def is_valid_invite_code(db: session, invite_code: str) -> Tuple[bool, Optional[int], Optional[str], Optional[str]]:
    """
    초대 코드의 유효성을 검사하고, 
    해당 유저의 user_id, username, profile_picture를 반환합니다.
    """
    user = get_user_by_invite_code(db, invite_code)
    if user:
        return True, user.user_id, user.username, user.profile_picture
    else:
        return False, None, None, None


def create_new_user(email: str, name: str, invite_code: str):
    # 사용자 생성 로직
    pass
