from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date


Base = declarative_base()


class QuestionModel(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True,  index=True, unique=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    date = Column(Date, nullable=False)
