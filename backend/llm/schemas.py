FINANCIAL_REPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "health_score": {"type": "number"},
        "summary": {"type": "string"},
        "projected_cash_flow_6_months": {
            "type": "array",
            "items": {"type": "number"}
        },
        "risks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "risk": {"type": "string"},
                    "mitigation": {"type": "string"}
                }
            }
        },
        "cost_saving_recommendations": {
            "type": "array",
            "items": {"type": "string"}
        },
        "recommended_products": {
            "type": "array",
            "items": {"type": "string"}
        }
    }
}
