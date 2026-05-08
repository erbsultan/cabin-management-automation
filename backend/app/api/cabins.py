from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cabin import Cabin
from app.schemas.cabin import CabinRead

router = APIRouter(
    prefix="/api/cabins",
    tags=["cabins"],
)


@router.get("", response_model=list[CabinRead])
def get_cabins(db: Session = Depends(get_db)):
    query = select(Cabin).order_by(Cabin.number)
    cabins = db.scalars(query).all()
    return cabins

