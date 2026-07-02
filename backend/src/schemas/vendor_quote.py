from pydantic import BaseModel

class VendorQuoteCreate(BaseModel):
    request_id: int
    vendor_id: int
    price: float
    delivery_days: int
    notes: str | None = None