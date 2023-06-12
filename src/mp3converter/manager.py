import os
from os import path
from uuid import uuid4

from fastapi import UploadFile, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from config import DBConfig
from src.mp3converter.model import UserModel, AudioModel
from src.mp3converter.schemas import UserSchema


async def create_user(username: str, db: Session):
    user_uuid = str(uuid4())
    user_model = UserModel(name=username, uuid=user_uuid)
    db.add(user_model)
    db.commit()
    return UserSchema(id=user_model.id, uuid=user_model.uuid)


async def convert(user: str, user_uuid: str, file: UploadFile, db: Session):
    if path.splitext(file.filename)[1] != ".wav":
        raise HTTPException(status_code=422, detail="Bad file extension.")

    user_in_base = db.query(UserModel).filter((UserModel.id == user) & (UserModel.uuid == user_uuid)).first()
    if not user_in_base:
        raise HTTPException(status_code=403, detail="Incorrect user id or token.")

    audio_uuid = str(uuid4())
    audio_model = AudioModel(uuid=audio_uuid, user_id=user)
    db.add(audio_model)
    db.commit()

    if not os.path.exists("mp3files"):
        os.mkdir(path="mp3files")

    with open(f"mp3files/id_{audio_model.id}_user_{user}.mp3", "ab") as f:
        f.write(file.file.read())

    return f"http://localhost:8000/record?id={audio_model.id}&user={user}"


async def download(id: int, user: int):
    return FileResponse(path=f"mp3files/id_{id}_user_{user}.mp3",
                        filename=f"id_{id}_user_{user}.mp3",
                        media_type='application/octet-stream')
