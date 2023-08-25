from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv('/app/.env.backend')

# 환경변수 가져오기
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'db')  # 디폴트로 'db' 사용
DATABASE_PORT = os.environ.get('DATABASE_PORT', '3307')  # 디폴트로 '3307' 사용
middlewareKey = os.environ.get('middlewareKey')

# google oauth 관련 환경변수
GOOGLE_CLIENT_ID = os.environ.get('client_id')
GOOGLE_CLIENT_SECRET = os.environ.get('client_secret')
REDIRECT_URI = os.environ.get(
    'redirect_uri', 'http://localhost:8000/login/callback')
# 첫번째 인자가 조회되지 않으면 디폴트로 두번째 인자 URI 사용
GOOGLE_AUTH_URI = os.environ.get('auth_uri')
GOOGLE_TOKEN_URI = os.environ.get('token_uri')
GOOGLE_AUTH_PROVIDER_X509_CERT_URL = os.environ.get(
    'auth_provider_x509_cert_url')

# DATABASE_URL 구성
DATABASE_URL = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

# storage 구성
STORAGE_BACKEND=os.environ.get('STORAGE_BACKEND', 'local')

# spotify api 용 환경 변수
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')