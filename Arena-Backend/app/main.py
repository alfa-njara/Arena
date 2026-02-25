from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.models.base import Base
from app.models.project import Project as ProjectModel
from app.routers import project

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Arena Backend API")

# CORS (React Native)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router
app.include_router(project.router)
