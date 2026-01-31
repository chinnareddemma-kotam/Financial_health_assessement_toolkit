def calculate_health_score(row):
    revenue = row.get("Revenue", 0)
    profit_margin = row.get("Profit_Margin", 0)
    cost_ratio = row.get("Cost_Ratio", 0)
    net_profit = row.get("NetProfit", 0)

    score = 50  # base score

    # Profit Margin contribution
    if profit_margin >= 0.30:
        score += 25
    elif profit_margin >= 0.15:
        score += 15
    else:
        score -= 10

    # Cost efficiency
    if cost_ratio < 0.6:
        score += 15
    elif cost_ratio > 0.8:
        score -= 10

    # Net profit check
    if net_profit < 0:
        score -= 20

    # Clamp score between 0–100
    return max(0, min(100, score))
