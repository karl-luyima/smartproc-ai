from fastapi import FastAPI

from backend.src.api.routes import procurement, quotes, vendor
from backend.src.core.database import Base, engine
from backend.src.api.routes import ai

app = FastAPI(title="SmartProc AI")

Base.metadata.create_all(bind=engine)

app.include_router(ai.router)
app.include_router(vendor.router)
app.include_router(quotes.router)
app.include_router(procurement.router)


@app.get("/") 
def root():
    return {"status": "SmartProc running"}