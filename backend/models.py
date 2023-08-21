from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    # This can be a link to the image or blob data
    profile_picture = Column(String(255))
    one_line_intro = Column(String(255))
    invited_by = Column(Integer, ForeignKey('users.user_id'))

    # This establishes a relationship for easily accessing who invited this user
    inviter = relationship("User", remote_side=[user_id])


class InvitedEmail(Base):
    __tablename__ = "invited_emails"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invitee_email = Column(String(255), nullable=False)
    invited_by = Column(Integer, ForeignKey('users.user_id'))


class SNSLink(Base):
    __tablename__ = "sns_links"

    link_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    platform = Column(String(100))
    link_url = Column(String(255))
    visit_count = Column(Integer, default=0)


class InviteHistory(Base):
    __tablename__ = "invite_history"

    history_id = Column(Integer, primary_key=True)
    inviter_id = Column(Integer, ForeignKey('users.user_id'))
    invitee_id = Column(Integer, ForeignKey('users.user_id'))
    date_invited = Column(DateTime, default=datetime.datetime.utcnow)


class TourDates(Base):
    __tablename__ = "tour_dates"

    tour_date_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    location = Column(String(255), nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    ticket_link = Column(String(255))


class PageViews(Base):
    __tablename__ = "page_views"

    view_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    date_viewed = Column(DateTime, default=datetime.datetime.utcnow)
    referrer_url = Column(String(255))  # To know where the visitor came from
    # To know where the visitor went, if they clicked on an SNS link
    destination_url = Column(String(255))


class MusicIntro(Base):
    __tablename__ = "music_intro"

    intro_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    intro_text = Column(Text, nullable=False)


class LinkFlow(Base):
    __tablename__ = "link_flow"

    flow_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    initial_url = Column(String(255), nullable=False)
    subsequent_url = Column(String(255), nullable=False)
