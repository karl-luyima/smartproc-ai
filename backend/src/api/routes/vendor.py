from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.core.dependencies import get_db
from backend.src.models.vendor import Vendor
from backend.src.schemas.vendor import VendorCreate

router = APIRouter(prefix="/vendors", tags=["Vendors"])


@router.post("/")
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    new_vendor = Vendor(**vendor.dict())
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor


@router.get("/")
def get_vendors(db: Session = Depends(get_db)):
    return db.query(Vendor).all()