import datetime

from pydantic import BaseModel


class QuestionSchema(BaseModel):
    id: int
    question: str
    answer: str
    date: datetime.date
