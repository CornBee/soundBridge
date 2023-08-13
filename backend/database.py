import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

Base = declarative_base()

MAX_RETRIES = 3
RETRY_INTERVAL = 10  # seconds

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 연결 재시도 로직
for _ in range(MAX_RETRIES):
    try:
        # 이 연결 시도는 DB가 준비되었는지 확인하기 위한 것입니다.
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
