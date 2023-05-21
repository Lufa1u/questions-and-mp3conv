from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy.orm import declarative_base

load_dotenv()


class DBConfig:
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")


def get_db():
    engine = create_engine(url=f"postgresql://{DBConfig.DB_USER}:{DBConfig.DB_PASS}@{DBConfig.DB_HOST}/{DBConfig.DB_NAME}")
    session = sessionmaker(engine)
    return session()

