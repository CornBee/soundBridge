import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base, User, InvitedEmail, SNSLink, InviteHistory, TourDates, PageViews, MusicIntro, LinkFlow

MAX_RETRIES = 10
RETRY_INTERVAL = 10  # seconds

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# 데이터베이스 연결 재시도 로직
for _ in range(MAX_RETRIES):
    try:
        connection = engine.connect()
        connection.close()
        print("Successfully connected to the database.")
        break
    except OperationalError as e:
        print(f"Error while connecting: {e}")
        print(
            f"Database not ready yet. Retrying in {RETRY_INTERVAL} seconds...")
        time.sleep(RETRY_INTERVAL)
else:
    raise Exception(
        "Could not establish a connection to the database after multiple retries.")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
