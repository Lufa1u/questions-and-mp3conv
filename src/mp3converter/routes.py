from fastapi import APIRouter, Depends, UploadFile
from config import get_db
from src.mp3converter import manager
from sqlalchemy.orm import Session
from src.mp3converter.schemas import UserSchema


router = APIRouter()


@router.post(path="/create_user", response_model=UserSchema)
async def create_user(username: str, db: Session = Depends(get_db)):
    return await manager.create_user(username=username, db=db)


@router.post(path="/convert", response_model=str)
async def convert(user: str, user_uuid: str, file: UploadFile, db: Session = Depends(get_db)):
    return await manager.convert(user=user, user_uuid=user_uuid, file=file, db=db)
