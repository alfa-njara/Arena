# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Import correct maintenant que models est dans app/
from app.models.base import Base
from app.models.user import User as UserModel
from app.models.project import Project as ProjectModel
from app.models.event import Event as EventModel 

# --- Config Base de données ---
DATABASE_URL = "postgresql+psycopg2://arena_user:arena@localhost:5432/arena_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Crée les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Arena Backend API")

# --- Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoints ---
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(UserModel).all()

@app.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(ProjectModel).all()

@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(EventModel).all()

@app.post("/projects/{project_id}/like")
def like_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.likes += 1
    db.commit()
    db.refresh(project)
    return project