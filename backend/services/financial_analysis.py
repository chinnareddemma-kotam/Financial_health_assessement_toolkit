from ..llm.gemini_client import GeminiClient 
from ..llm.schemas import FINANCIAL_REPORT_SCHEMA
from ..llm.prompts import FINANCIAL_ANALYSIS_SYSTEM_PROMPT

async def run_llm_analysis(industry, raw_data, metrics, language):
    client = GeminiClient()

    prompt = FINANCIAL_ANALYSIS_SYSTEM_PROMPT(
        industry=industry,
        raw_data=raw_data,
        calculated_metrics=metrics,
        lang=language
    )

    response = await client.generate_financial_report(
        prompt=prompt,
        schema=FINANCIAL_REPORT_SCHEMA
    )

    return response
