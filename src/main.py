from fastapi import FastAPI

from src.core.database import Base, engine
from src.api.routes import ai, vendor, quotes, procurement

app = FastAPI(title="SmartProc AI")

Base.metadata.create_all(bind=engine)

app.include_router(ai.router)
app.include_router(vendor.router)
app.include_router(quotes.router)
app.include_router(procurement.router)


@app.get("/")
def root():
    return {"status": "SmartProc running"}