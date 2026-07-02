from datetime import datetime

class ProcurementAgent:

    def evaluate_vendors(self, quotes, vendors):
        """
        This is the AI decision engine for SmartProc.
        It compares vendors and recommends the best one.
        """

        scored_results = []

        best_vendor = None
        best_score = -1
        reasoning = []

        for quote in quotes:

            vendor = next(
                (v for v in vendors if v["id"] == quote["vendor_id"]),
                None
            )

            if not vendor:
                continue

            # --- SCORING LOGIC (AI decision rules) ---
            price_score = 1000 / quote["price"]  # lower price = better
            delivery_score = 1 / quote["delivery_days"]  # faster delivery = better
            rating_score = vendor["rating"] * 10

            total_score = (price_score * 0.4) + (delivery_score * 0.3) + (rating_score * 0.3)

            result = {
                "vendor_id": vendor["id"],
                "vendor_name": vendor["name"],
                "price": quote["price"],
                "delivery_days": quote["delivery_days"],
                "score": round(total_score, 2)
            }

            scored_results.append(result)

            reasoning.append(
                f"{vendor['name']} scored {round(total_score,2)} "
                f"(price={quote['price']}, delivery={quote['delivery_days']} days, rating={vendor['rating']})"
            )

            if total_score > best_score:
                best_score = total_score
                best_vendor = result

        return {
            "best_vendor": best_vendor,
            "all_scores": scored_results,
            "reasoning": reasoning,
            "confidence": round(best_score, 2),
            "generated_at": datetime.utcnow().isoformat()
        }