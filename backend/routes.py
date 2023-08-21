from fastapi import APIRouter, Depends
from models import SNSLink, User
from scraper import get_soundcloud_track_id
from database import SessionLocal

router = APIRouter()

@router.get("/top-track-id/{username}-{user_id}")
async def get_top_track_id(username: str, user_id: int, session: SessionLocal = Depends(SessionLocal)):
    user = session.query(User).filter_by(user_id=user_id).first()
    if not user or user.username != username:
        return {"error": "User not found."}

    soundcloud_link = session.query(SNSLink).filter_by(user_id=user_id, platform="soundcloud").first()
    if not soundcloud_link:
        return {"error": "SoundCloud link not found for the user."}

    track_id = await get_soundcloud_track_id(soundcloud_link.link_url)
    return {"track_id": track_id}