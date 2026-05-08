from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentRead

router = APIRouter(
    prefix="/api/students",
    tags=["students"],
)


@router.get("", response_model=list[StudentRead])
def get_students(db: Session = Depends(get_db)):
    query = select(Student).order_by(Student.login)
    return db.scalars(query).all()


@router.get("/{login}", response_model=StudentRead)
def get_student(login: str, db: Session = Depends(get_db)):
    student = db.scalar(select(Student).where(Student.login == login))

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student


@router.post("", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    existing_student = db.scalar(
        select(Student).where(Student.login == payload.login)
    )

    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student already exists",
        )

    student = Student(
        login=payload.login,
        full_name=payload.full_name,
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student
