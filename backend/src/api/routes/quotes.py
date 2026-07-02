from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.core.dependencies import get_db
from backend.src.models.vendor_quote import VendorQuote
from backend.src.schemas.vendor_quote import VendorQuoteCreate

router = APIRouter(prefix="/quotes", tags=["Quotes"])


@router.post("/")
def add_quote(quote: VendorQuoteCreate, db: Session = Depends(get_db)):
    new_quote = VendorQuote(**quote.dict())
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return new_quote


@router.get("/")
def get_quotes(db: Session = Depends(get_db)):
    return db.query(VendorQuote).all()