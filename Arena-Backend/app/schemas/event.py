from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    date: datetime | None = None
    location: str | None = None
    image: str | None = None

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True