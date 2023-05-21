from fastapi import APIRouter, Depends
from uuid import uuid4
from config import get_db
from src.mp3converter import manager
from sqlalchemy.orm import Session
from src.mp3converter.schemas import UserSchema


router = APIRouter()


@router.post(path="/create_user", response_model=UserSchema)
async def create_user(username: str, db: Session = Depends(get_db)):
    user_uuid = str(uuid4())
    return await manager.create_user(username=username, user_uuid=user_uuid, db=db)
