from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.dependencies import get_db
from src.models.vendor import Vendor
from src.models.vendor_quote import VendorQuote
from src.agent.procurement_agent import ProcurementAgent

router = APIRouter(prefix="/ai", tags=["AI Procurement"])


@router.get("/evaluate/{request_id}")
def evaluate_request(request_id: int, db: Session = Depends(get_db)):

    # Get all quotes for this request
    quotes = db.query(VendorQuote).filter(
        VendorQuote.request_id == request_id
    ).all()

    # Get all vendors
    vendors = db.query(Vendor).all()

    # Convert to simple dicts
    quote_data = [
        {
            "vendor_id": q.vendor_id,
            "price": q.price,
            "delivery_days": q.delivery_days
        }
        for q in quotes
    ]

    vendor_data = [
        {
            "id": v.id,
            "name": v.name,
            "rating": v.rating
        }
        for v in vendors
    ]

    # Run AI engine
    agent = ProcurementAgent()
    result = agent.evaluate_vendors(quote_data, vendor_data)

    return result