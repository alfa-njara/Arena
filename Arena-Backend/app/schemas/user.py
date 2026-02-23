from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    number: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True