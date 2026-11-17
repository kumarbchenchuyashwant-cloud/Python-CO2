def subsidy_separate(units, ration_card, member_above_80):
    """Several separate if statements - a household can receive TWO subsidies."""
    result = []
    if units <= 100:
        result.append("FULL")
    if 101 <= units <= 200 and ration_card:
        result.append("PARTIAL")
    if units <= 200 and ration_card:            
        result.append("PARTIAL")
    if units > 200 and member_above_80:
        result.append("SENIOR")
    return result or ["NONE"]


def subsidy_elif(units, ration_card, member_above_80):
    """if-elif-else - exactly one decision is possible."""
    if units <= 100:
        return "FULL"
    elif 101 <= units <= 200 and ration_card:
        return "PARTIAL"
    elif units > 200 and member_above_80:
        return "SENIOR"
    else:
        return "NONE"