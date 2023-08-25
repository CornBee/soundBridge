import spotipy
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from database import SessionLocal
from models import SNSLink
from spotipy.oauth2 import SpotifyClientCredentials
import re

# Spotify API 인증
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))

def get_album_artwork(user_id):
    # 아티스트 스포티파이 id 가져오기
    session = SessionLocal()
    user_sns = session.query(SNSLink).filter(
        SNSLink.user_id == user_id, 
        SNSLink.platform == "spotify"
    ).order_by(SNSLink.link_id.asc()).one_or_none()

    if not user_sns:
        print(f"No user_sns found with id {user_id}")
        return
    else:
        spotify_url = user_sns.link_url
        print("spotify_url : " + spotify_url)
        artist_spotify_id = re.search(r'\/artist\/([0-9a-zA-Z]+)', spotify_url).group(1)
        print("artist_spotify_id : " + artist_spotify_id)
    
    # 아티스트의 앨범과 싱글 정보 가져오기
    albums_and_singles = sp.artist_albums(artist_spotify_id, album_type='album,single')
    
    # 앨범과 싱글들의 아트워크 URL 가져오기
    artwork_urls = []
    for item in albums_and_singles['items']:
        artwork_url = item['images'][0]['url']  # 일반적으로 가장 큰 이미지
        artwork_urls.append(artwork_url)
        
    return artwork_urls