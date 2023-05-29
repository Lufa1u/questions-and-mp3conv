from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config import get_db
from src.questions import manager

router = APIRouter()


@router.post(path="/get_questions")
async def get_questions(questions_num: int, db: Session = Depends(get_db)):
    return await manager.get_questions(questions_num=questions_num, db=db)
