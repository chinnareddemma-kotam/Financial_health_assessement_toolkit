from fastapi import APIRouter
from services.financial_analysis import run_llm_analysis

router = APIRouter()

@router.post("/analyze")
async def analyze_business(payload: dict):
    llm_result = await run_llm_analysis(
        industry=payload["industry"],
        raw_data=payload["raw_data"],
        metrics=payload["metrics"],
        language=payload.get("lang", "en")
    )

    return {
        "status": "success",
        "llm_analysis": llm_result
    }
