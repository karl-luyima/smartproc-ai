class ProcurementAgent:

    def evaluate_quotes(self, quotes):
        """
        Simple scoring system (we will later replace with LangGraph + LLM)
        """

        best_vendor = None
        best_score = 0

        results = []

        for q in quotes:
            score = (
                (1 / q["price"]) * 40 +
                (1 / q["delivery_days"]) * 30 +
                (q["rating"]) * 30
            )

            results.append({
                "vendor": q["vendor"],
                "score": score
            })

            if score > best_score:
                best_score = score
                best_vendor = q["vendor"]

        return {
            "best_vendor": best_vendor,
            "score": best_score,
            "ranking": results
        }