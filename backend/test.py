#!/usr/bin/env python3
from models import User, InvitedEmail
from database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from apis import get_album_artwork

def insert_test_data():
    db = SessionLocal()

    try:
        # Check if the inviter user exists
        inviter_email = "inviter@example.com"

        # Create inviter user
        print("Inviter not found. Creating a new one...")  # 로깅 추가
        inviter = User(username="inviter_user", email=inviter_email)
        db.add(inviter)
        db.commit()
        print("Inviter created successfully.")  # 로깅 추가

        # Check if the invitee exists in the InvitedEmail table
        invitee_email = "cornbee80014@gmail.com"

        # Create an InvitedEmail entry
        print("Invitee not found. Creating a new one...")  # 로깅 추가
        new_invitee = InvitedEmail(
            invitee_email=invitee_email, invited_by=inviter.user_id)
        db.add(new_invitee)
        db.commit()
        print("Invitee created successfully.")  # 로깅 추가

        

    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")  # 에러 메시지 출력
        db.rollback()  # 롤백 수행

    finally:
        db.close()

print(get_album_artwork(3))

