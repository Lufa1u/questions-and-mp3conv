from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

path_to_folder = os.environ.get("PATH_TO_FOLDER")


class DBConfig:
    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PASS = os.environ.get("POSTGRES_PASSWORD")
    DB_HOST = os.environ.get("POSTGRES_HOST")
    DB_PORT = os.environ.get("POSTGRES_PORT")
    DB_NAME = os.environ.get("POSTGRES_DB")


def get_db():
    engine = create_engine(url=f"postgresql://{DBConfig.DB_USER}:{DBConfig.DB_PASS}@{DBConfig.DB_HOST}/{DBConfig.DB_NAME}")
    session = sessionmaker(engine)
    return session()

