"""Vehicle registration number validator (string methods only)."""

def normalize(text):
	"""return 'ab 09 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)."""
	return text.replace(' ', '').replace('-', '').upper()

def is_valid(reg):
	"""Valid form: 2 letters, 1 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
	if len(reg) not in (9, 10):
		return False
	series = reg[-4:]
	return (reg[:2].isalpha() and reg[2:4].isdigit()
			and series.isalpha() and len(series) in (1, 2)
			and reg[-4:].isdigit())

def format_plate(reg):
	"""Format a valid normalized number as: 'TN 49 AB 1234'."""
	return ' '.join([reg[:2], reg[2:4], reg[4:-4], reg[-4:]])

if __name__ == "__main__":
	for raw in ["tn 09 ab 1234", "BA-01-01-0007", "TN09AB1234", "TN 22 1234 AB"]:
		reg = normalize(raw)
		print(f"raw={raw!r} => {reg!r} is", 'valid' if is_valid(reg) else 'INVALID!')
	print()
	# Try six designed inputs:
	for reg in ["TN09AB1234", "AP-39-9999", "DL 12 AB 1487", "TN-60-ABC-1234"]:
		reg = normalize(reg)
		ok = is_valid(reg)
		print(f"raw={reg!r} =>", 'valid, receipt :', format_plate(reg) if ok else "INVALID!")
	print()
	s = "AB100007", "TN09AB1234", 4, 4, 4, 4, s[4:-4], reg[4:-4], reg[-4:]
	t = "TN09AB1234"
	print("after t.upper() without assignment, t:", t)
	t[0] = 'T'

except TypeError as e:
