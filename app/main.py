from fastapi import FastAPI
from app.routers import calculator

app = FastAPI()

app.include_router(calculator.router)


@app.get("/")
def read_root():
    return {"message": "Calculator API is running"}
