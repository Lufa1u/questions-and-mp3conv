from sqlalchemy import select
from sqlalchemy.orm import Session
import aiohttp
from src.questions.model import QuestionModel
import datetime
from src.questions.schemas import QuestionSchema


async def get_questions(questions_num: int, db: Session, all_question_ids: list[int] = None):
    questions = []
    non_unique = 0
    if not all_question_ids:
        all_question_ids = await get_all_question_ids(db=db)

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://jservice.io/api/random?count={abs(questions_num)}') as response:
            items = await response.json()

    for item in items:
        if item["id"] not in all_question_ids:
            question = QuestionModel(id=item["id"], question=item["question"], answer=item["answer"],
                                     date=datetime.datetime.strptime(item["airdate"], "%Y-%m-%dT%H:%M:%S.%fZ"))
            all_question_ids.append(question.id)
            questions.append(question)
        else:
            non_unique += 1
            continue
    db.add_all(questions)
    if non_unique == 100:
        return None
    if non_unique:
        return await get_questions(questions_num=non_unique, db=db, all_question_ids=all_question_ids)
    db.commit()
    return QuestionSchema(id=question.id, question=question.question, answer=question.answer, date=question.date)


async def get_all_question_ids(db: Session):
    return db.execute(select(QuestionModel.id)).scalars().all()
