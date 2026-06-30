def load_data(state):
    """
    Loads quotes + vendor data (already passed from API)
    """
    return state


def evaluate_vendors(state):
    quotes = state["quotes"]
    vendors = state["vendors"]

    results = []
    best = None
    best_score = -1

    for q in quotes:
        vendor = next(v for v in vendors if v["id"] == q["vendor_id"])

        score = (
            (1000 / q["price"]) * 0.4 +
            (1 / q["delivery_days"]) * 0.3 +
            (vendor["rating"] * 10) * 0.3
        )

        result = {
            "vendor_id": vendor["id"],
            "vendor_name": vendor["name"],
            "score": round(score, 2)
        }

        results.append(result)

        if score > best_score:
            best_score = score
            best = result

    state["scores"] = results
    state["best_vendor"] = best

    return state


def generate_reasoning(state):
    best = state["best_vendor"]

    state["reasoning"] = [
        f"Evaluated {len(state['scores'])} vendors",
        f"Best vendor selected: {best['vendor_name']}",
        f"Score: {best['score']}"
    ]

    return state


def finalize(state):
    return {
        "best_vendor": state["best_vendor"],
        "all_scores": state["scores"],
        "reasoning": state["reasoning"]
    }