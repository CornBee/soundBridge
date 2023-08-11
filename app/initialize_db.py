from database import engine, SessionLocal, Base
from models import User

Base.metadata.create_all(engine)

session = SessionLocal()

# 예제: 사용자 추가
new_user = User(username="test", password="testpassword",
                email="test@email.com", invite_code="TEST1234")
session.add(new_user)
session.commit()
