from pydantic import BaseModel
from datetime import datetime

class ProjectBase(BaseModel):
    title: str
    description: str | None = None
    stack: str | None = None
    contact: str | None = None
    url: str | None = None
    icon: str | None = None
    comment: str | None = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    likes: int
    created_at: datetime

    class Config:
        orm_mode = True