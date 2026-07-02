def load_data(state):
    return state


def evaluate_vendors(state):
    quotes = state["quotes"]
    vendors = state["vendors"]

    results = []
    best = None
    best_score = -1

    for q in quotes:

        vendor = next((v for v in vendors if v["id"] == q["vendor_id"]), None)
        if not vendor:
            continue

        price_score = max(0, 100 - (q["price"] / 10))
        delivery_score = max(0, 100 - (q["delivery_days"] * 10))
        rating_score = vendor["rating"] * 20

        urgency = state.get("urgency", "normal")

        if urgency == "high":
            weights = {"price": 0.3, "delivery": 0.5, "rating": 0.2}
        elif urgency == "low":
            weights = {"price": 0.5, "delivery": 0.2, "rating": 0.3}
        else:
            weights = {"price": 0.4, "delivery": 0.3, "rating": 0.3}

        total = (
            price_score * weights["price"] +
            delivery_score * weights["delivery"] +
            rating_score * weights["rating"]
        )

        risk = []

        if q["price"] > 900:
            risk.append("High cost risk")

        if q["delivery_days"] > 10:
            risk.append("Severe delay risk")

        if vendor["rating"] < 3.5:
            risk.append("Unreliable vendor risk")

        item = {
            "vendor_id": vendor["id"],
            "vendor_name": vendor["name"],
            "score": round(total, 2),
            "price": q["price"],
            "delivery_days": q["delivery_days"],
            "risk_flags": risk
        }

        results.append(item)

        if total > best_score:
            best_score = total
            best = item

    if best is None:
        state["scores"] = []
        state["best_vendor"] = None
        state["confidence"] = 0
        return state

    state["scores"] = results
    state["best_vendor"] = best
    state["confidence"] = float(round(best_score, 2)) if best_score > 0 else 0.0

    return state


def generate_reasoning(state):
    best = state.get("best_vendor")
    scores = state.get("scores", [])
    confidence = state.get("confidence", 0)

    if not best:
        state["reasoning"] = [
            "No valid vendor selected",
            "Check input data"
        ]
        return state

    state["reasoning"] = [
        f"Evaluated {len(scores)} vendors",
        f"Selected {best.get('vendor_name')} with confidence {confidence}",
        "Decision based on cost, delivery, and reliability"
    ]

    return state


def finalize(state):

    state["result"] = {
        "best_vendor": state.get("best_vendor"),
        "scores": state.get("scores", []),
        "confidence": state.get("confidence", 0.0),
        "reasoning": state.get("reasoning", []),
        "risk_summary": [
            item.get("risk_flags", [])
            for item in state.get("scores", [])
        ]
    }

    return state


def decision_router(state):
    confidence = state.get("confidence", 0)

    if confidence < 50:
        state["flag"] = "REVIEW_REQUIRED"
    else:
        state["flag"] = "APPROVED"

    return state