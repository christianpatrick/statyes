import os
from dotenv import load_dotenv
from fastapi import FastAPI
from .routers import events

if os.environ.get("PYTHON_ENV") == "development":
    load_dotenv()

app = FastAPI()
app.include_router(events.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Statyes API!"}
