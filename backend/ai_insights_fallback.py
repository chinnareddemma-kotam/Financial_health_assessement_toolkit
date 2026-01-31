def fallback_ai_insights(metrics: dict):
    score = metrics.get("avg_health_score", 0)
    margin = metrics.get("avg_profit_margin", 0)

    if score >= 80:
        status = "strong"
    elif score >= 60:
        status = "stable"
    else:
        status = "at risk"

    return f"""
FINANCIAL HEALTH SUMMARY:
The business portfolio shows a {status} financial position.

KEY OBSERVATIONS:
• Average health score: {score}
• Profit margin trend: {round(margin * 100, 2)}%

RECOMMENDATIONS:
• Maintain operating cost discipline
• Improve receivable collection cycles
• Consider short-term working capital optimization

NOTE:
This insight is generated using deterministic financial rules when AI services are unavailable.
"""
