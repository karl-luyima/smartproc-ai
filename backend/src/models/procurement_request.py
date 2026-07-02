from sqlalchemy import Column, Integer, String, Text
from backend.src.core.database import Base

class ProcurementRequest(Base):
    __tablename__ = "procurement_requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(String, default="pending")