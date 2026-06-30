from fastapi import FastAPI
from src.core.database import Base, engine

from src.api.routes import procurement, vendor, quotes, ai

# 1. Create app FIRST (VERY IMPORTANT)
app = FastAPI(title="SmartProc AI")

# 2. Create DB tables
Base.metadata.create_all(bind=engine)

# 3. Register routers AFTER app is created
app.include_router(procurement.router)
app.include_router(vendor.router)
app.include_router(quotes.router)
app.include_router(ai.router)


@app.get("/")
def root():
    return {"message": "SmartProc AI is running"}