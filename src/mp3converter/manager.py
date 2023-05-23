from os import path
from uuid import uuid4

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from config import path_to_folder, DBConfig
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
    with open(f"{path_to_folder}/{audio_uuid}.mp3", "ab") as f:
        f.write(file.file.read())

    audio_model = AudioModel(uuid=audio_uuid, user_id=user)
    db.add(audio_model)
    db.commit()
    return f"http://{DBConfig.DB_HOST}:{DBConfig.DB_PORT}/record?id={audio_model.id}&user={user}"
