def generate_report(state):
    best = state["best_vendor"]

    return {
        "title": "PROCUREMENT DECISION REPORT",
        "best_vendor": best["vendor_name"],
        "score": best["score"],
        "reasoning": state["reasoning"],
        "summary": f"Recommended vendor is {best['vendor_name']} based on scoring model."
    }