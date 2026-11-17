# Nested version
def check_benefit_nested(units, ration_card, member_above_80):
	if units <= 100:
		return "FULL"
	else:
		if units <= 200:
			if ration_card:
				return "PARTIAL"
			else:
				return "NONE"
		else:
			if member_above_80:
				return "SENIOR"
			return "NONE"

# Condensed version (chosen)
def check_benefit_condensed(units, ration_card, member_above_80):
	if units <= 100:
		return "FULL"
	elif 101 <= units <= 200 and ration_card:
		return "PARTIAL"
	elif units > 200 and member_above_80:
		return "SENIOR"
	else:
		return "NONE"
