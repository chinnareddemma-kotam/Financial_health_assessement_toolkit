# backend/services/run_llm_analysis.py

from backend.llm.gemini_client import GeminiClient
from backend.llm.prompts import get_analysis_prompt
from backend.llm.schemas import FINANCIAL_REPORT_SCHEMA

async def run_llm_analysis(industry: str, raw_data: str, metrics: dict, language: str):
    """
    Runs the Gemini LLM to generate a financial report.
    """
    client = GeminiClient()

    # Build the prompt for the LLM
    prompt = get_analysis_prompt(
        industry=industry,
        raw_data=raw_data,
        calculated_metrics=metrics,
        lang=language
    )

    # Generate report from LLM
    response = await client.generate_financial_report(
        prompt=prompt,
        schema=FINANCIAL_REPORT_SCHEMA
    )

    return response
