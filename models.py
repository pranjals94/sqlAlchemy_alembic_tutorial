import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, BIGINT, Time, Date
from sqlalchemy.orm import relationship


from database import Base

class Person(Base):
    __tablename__ = "person"
    id = Column(BIGINT, primary_key=True, index=True)  # index helps make queries faster
    name = Column(String(100))
    phone_no = Column(String(13))
    gender = Column(String(10))


class User(Base):
    __tablename__ = "user"

    id = Column(BIGINT, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(200))
    date_created = Column(DateTime, default=datetime.datetime.now())

    # person_id = Column(BIGINT, ForeignKey("person.id")) # create this through alembic
    person = relationship("Person", backref="owner")  # refer sqlAlchemy documentation, Using the legacy ‘backref’
    # relationship parameter
