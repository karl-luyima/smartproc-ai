def load_data(state):
    # Just passes state through (can be extended later)
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

        # -----------------------------
        # SCORING ENGINE
        # -----------------------------

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

        # -----------------------------
        # RISK ENGINE
        # -----------------------------

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

    # -----------------------------
    # SAFETY CHECK (IMPORTANT)
    # -----------------------------

    if best is None:
        state["scores"] = []
        state["best_vendor"] = None
        state["confidence"] = 0
        return state

    # -----------------------------
    # FINAL STATE OUTPUT
    # -----------------------------

    state["scores"] = results
    state["best_vendor"] = best
    state["confidence"] = round(best_score, 2)

    return state


def generate_reasoning(state):
    best = state["best_vendor"]
    scores = state["scores"]

    state["reasoning"] = [
        f"Evaluated {len(scores)} vendors",
        f"Selected {best['vendor_name']} with confidence {state['confidence']}",
        "Decision based on cost efficiency, delivery speed, and vendor reliability"
    ]

    return state


def finalize(state):
    """
    Wraps final output into structured result for API consumption
    """

    state["result"] = {
        "best_vendor": state["best_vendor"],
        "scores": state["scores"],
        "confidence": state["confidence"],
        "reasoning": state["reasoning"],
        "risk_summary": [
            item["risk_flags"]
            for item in state["scores"]
            if item["risk_flags"]
        ]
    }

    return state


def decision_router(state):
    """
    Decision gate for approval or manual review
    """

    confidence = state.get("confidence", 0)

    if confidence < 50:
        state["flag"] = "REVIEW_REQUIRED"
    else:
        state["flag"] = "APPROVED"

    return state