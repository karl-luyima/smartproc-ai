from fastapi import FastAPI
from src.core.database import Base, engine
from src.api.routes import procurement

app = FastAPI(title="SmartProc AI")

# Create database tables
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(procurement.router)

@app.get("/")
def root():
    return {"message": "SmartProc AI is running"}