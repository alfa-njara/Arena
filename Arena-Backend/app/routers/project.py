from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..models.project import Project as ProjectModel
from ..schemas.project import ProjectCreate, Project

router = APIRouter(prefix="/projects", tags=["projects"])

# CREATE
@router.post("/", response_model=Project)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = ProjectModel(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# READ ALL
@router.get("/", response_model=list[Project])
def get_projects(db: Session = Depends(get_db)):
    print("📦 GET /projects")
    return db.query(ProjectModel).order_by(ProjectModel.likes.desc()).all()

# LIKE
@router.post("/{project_id}/like", response_model=Project)
def like_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.likes += 1
    db.commit()
    db.refresh(project)
    return project