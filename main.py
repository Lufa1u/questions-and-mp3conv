from fastapi import FastAPI
from src.questions import routes as questions_routes
from src.mp3converter import routes as converter_routes


app = FastAPI()

# app.include_router(router=questions_routes.router, prefix="/questions", tags=["QUESTIONS"])
app.include_router(router=converter_routes.router, prefix="/record", tags=["RECORD"])

