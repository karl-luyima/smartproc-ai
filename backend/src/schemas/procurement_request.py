from pydantic import BaseModel

class ProcurementRequestCreate(BaseModel):
    title: str
    description: str
    quantity: int