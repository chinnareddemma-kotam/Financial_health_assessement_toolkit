from google import genai
import os

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-1.5-flash"

    def generate_insights(self, summary: dict) -> str:
        """
        Generate financial insights text from summary
        """
        prompt = f"""
You are a financial analyst.

Given this SME financial summary:
{summary}

Provide:
1. Overall financial health
2. Key risks
3. Clear actionable recommendations

Keep it simple and business-friendly.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text
