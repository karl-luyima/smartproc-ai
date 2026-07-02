from pydantic import BaseModel

class VendorCreate(BaseModel):
    name: str
    email: str | None = None
    rating: float = 3.0
    location: str | None = None