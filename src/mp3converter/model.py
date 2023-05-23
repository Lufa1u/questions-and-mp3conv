from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    uuid = Column(String, nullable=False)
    audios = relationship("AudioModel", back_populates="user")


class AudioModel(Base):
    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    uuid = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("UserModel", back_populates="audios")
