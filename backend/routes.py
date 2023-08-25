from fastapi import APIRouter, Depends, HTTPException
from models import SNSLink
from scraper import get_soundcloud_track_id, update_soundcloud_track_id
from external_apis import get_album_artwork
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.put("/profile/soundcloud/{user_id}")
async def update_and_get_top_track_id(user_id: int, session: Session = Depends(get_db)):
    # Fetch the user's SoundCloud link
    soundcloud_link = session.query(SNSLink).filter_by(user_id=user_id, platform="soundcloud").first()
    if not soundcloud_link:
        raise HTTPException(status_code=404, detail="SoundCloud link not found for the user.")

    # Fetch the top track ID using the scraper
    track_id = get_soundcloud_track_id(soundcloud_link.link_url)
    
    # Update the user's soundcloud_track_id in the database
    update_soundcloud_track_id(user_id, track_id)

    return {"track_id": track_id}

@router.get("/profile/album-artworks/{user_id}")
def get_album_artwork_urls(user_id: int):
    return get_album_artwork(user_id)
