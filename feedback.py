def interpret_impact(score):
    if score >= 2:
        return "Strong positive impact"
    elif score >= 0:
        return "Moderate impact"
    else:
        return "Negative impact"
