from sqlalchemy.orm import Session
from src.mp3converter.model import UserModel
from src.mp3converter.schemas import UserSchema


async def create_user(username: str, user_uuid: str, db: Session):
    user_model = UserModel(name=username, uuid=user_uuid)
    db.add(user_model)
    db.commit()
    return UserSchema(id=user_model.id, uuid=user_model.uuid)
