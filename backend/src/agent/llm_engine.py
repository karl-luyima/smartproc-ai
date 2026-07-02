from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


def explain_decision(best_vendor, scores, confidence):

    if client is None:
        return "OpenAI API key not configured."

    prompt = f"""
You are a procurement analyst.

Best vendor:
{best_vendor}

Confidence score:
{confidence}

All vendor scores:
{scores}

Explain clearly why this vendor is the best choice.
Be concise and business-focused.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI explanation failed: {str(e)}"