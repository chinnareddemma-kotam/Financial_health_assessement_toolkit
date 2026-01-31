from fastapi import APIRouter
from pydantic import BaseModel
from backend.llm.gemini_client import GeminiClient
import os

router = APIRouter()
client = GeminiClient(api_key=os.getenv("GEMINI_API_KEY"))

class FinancialRequest(BaseModel):
    prompt: str

@router.post("/analyze")
async def analyze_financials(req: FinancialRequest):
    result = await client.generate_financial_report(req.prompt)
    return {
        "analysis": result
    }
