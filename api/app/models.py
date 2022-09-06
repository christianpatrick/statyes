from pydantic import BaseModel
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

class Event(BaseModel):
    __tablename__ = "events"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(
        DateTime(timezone=False), server_default=text("now()"), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=False), server_default=text("now()"), nullable=False
    )

    updates = relationship("Update", back_populates="event")


class Update(BaseModel):
    __tablename__ = "updates"

    id = Column(BigInteger, primary_key=True, index=True)
    event_id = Column(BigInteger, ForeignKey("events.id"))
    published_at = Column(DateTime(timezone=False))
    created_at = Column(
        DateTime(timezone=False), server_default=text("now()"), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=False), server_default=text("now()"), nullable=False
    )

    event = relationship("Event", back_populates="updates")
