from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Update(BaseModel):
    published_at: datetime

    class Config:
        orm_mode = True
