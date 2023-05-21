from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    uuid = Column(String, nullable=False)
