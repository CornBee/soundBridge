from database import engine, SessionLocal, Base
from models import User

Base.metadata.create_all(engine)
session = SessionLocal()

# test.py를 실행시켜 예제 데이터를 추가
import test
test.insert_sample_data()