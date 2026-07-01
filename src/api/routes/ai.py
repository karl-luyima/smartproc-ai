from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.dependencies import get_db
from src.models.vendor import Vendor
from src.models.vendor_quote import VendorQuote

from src.agent.workflow import build_graph
from src.agent.report import generate_report
from src.agent.llm_engine import explain_decision
from src.agent.memory import save_decision

router = APIRouter(prefix="/ai", tags=["AI Agent"])


@router.get("/evaluate/{request_id}")
def evaluate(request_id: int, db: Session = Depends(get_db)):

    quotes = db.query(VendorQuote).filter(
        VendorQuote.request_id == request_id
    ).all()

    vendors = db.query(Vendor).all()

    quote_data = [
        {
            "vendor_id": q.vendor_id,
            "price": q.price,
            "delivery_days": q.delivery_days
        }
        for q in quotes
    ]

    vendor_data = [
        {
            "id": v.id,
            "name": v.name,
            "rating": v.rating
        }
        for v in vendors
    ]

    graph = build_graph()

    state = graph.invoke({
        "request_id": request_id,
        "quotes": quote_data,
        "vendors": vendor_data
    })

    result = state.get("result")

    if not result:
        return {
            "error": "AI workflow failed",
            "state": state
        }

    explanation = explain_decision(
        result["best_vendor"],
        result["scores"],
        result["confidence"]
    )

    report = generate_report(state)

    save_decision(request_id, result)

    return {
        "decision": result,
        "report": report,
        "ai_explanation": explanation
    }