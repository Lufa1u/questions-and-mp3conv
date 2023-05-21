from fastapi import APIRouter, Depends, UploadFile, HTTPException
from uuid import uuid4
from config import get_db
from src.mp3converter import manager
from sqlalchemy.orm import Session
from src.mp3converter.schemas import UserSchema
from os import path


router = APIRouter()


@router.post(path="/create_user", response_model=UserSchema)
async def create_user(username: str, db: Session = Depends(get_db)):
    user_uuid = str(uuid4())
    return await manager.create_user(username=username, user_uuid=user_uuid, db=db)


@router.post(path="/add_audio", response_model=str)
async def add_audio(user_id: int, user_uuid: str, file: UploadFile):
    if path.splitext(file.filename)[1] != ".wav":
        raise HTTPException(status_code=422, detail="Bad file extension.")
    pass