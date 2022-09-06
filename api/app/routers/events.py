from fastapi import APIRouter
import random, datetime, itertools
import os
from sqlalchemy.orm import Session

# from ..schema import Event as EventSchema
# from ..models import Event as EventModel

router = APIRouter()

@router.get("/events")
async def read_events():
    eventsDb = [
        {"name": "Foo"},
        {"name": "Bar"},
        {"name": os.environ.items()}
    ]

    return eventsDb
# @router.get("/events")
# async def event(db: Session):
    # return db.query(EventModel).all()


@router.get("/events/{eventId}")
async def read_event(eventId: int):
    levelArray = ["maintenance", "minor", "major", "critical"]
    singleEventDb = {
        "id": eventId,
        "name": "Foo",
        "level": random.choice(levelArray),
        # connections affected
        # updates here or in description?
        "event_date": datetime.datetime.now() + datetime.timedelta(5),
        "created_at": datetime.datetime.now() - datetime.timedelta(14),
        "updated_at": datetime.datetime.now() - datetime.timedelta(7),
        "created_by": 123,
        "updated_by": 456,
    }

    return list(itertools.repeat(singleEventDb, 100))
