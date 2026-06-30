from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.dependencies import get_db
from src.models.procurement_request import ProcurementRequest
from src.schemas.procurement_request import ProcurementRequestCreate

router = APIRouter(prefix="/procurement", tags=["Procurement"])


@router.post("/")
def create_request(req: ProcurementRequestCreate, db: Session = Depends(get_db)):
    new_req = ProcurementRequest(**req.dict())
    db.add(new_req)
    db.commit()
    db.refresh(new_req)
    return new_req


@router.get("/")
def get_requests(db: Session = Depends(get_db)):
    return db.query(ProcurementRequest).all()