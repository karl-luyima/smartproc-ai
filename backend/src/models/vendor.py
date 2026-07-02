from sqlalchemy import Column, Integer, String, Float
from backend.src.core.database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    rating = Column(Float, default=3.0)
    location = Column(String, nullable=True)