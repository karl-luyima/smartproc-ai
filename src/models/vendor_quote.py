from sqlalchemy import Column, Integer, Float, ForeignKey, String
from src.core.database import Base


class VendorQuote(Base):
    __tablename__ = "vendor_quotes"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("procurement_requests.id"), nullable=False)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)

    price = Column(Float, nullable=False)
    delivery_days = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)