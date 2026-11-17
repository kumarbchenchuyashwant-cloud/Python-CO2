"""Q1 - Building long text: += vs join vs f-string, StringIO alternative."""
import time, io, sys

def make_items(n): return [f"Item{{i}}:R{{i % 50}}" for i in range(n)]

def build_plus(parts):
	text = ""
	for p in parts:
		text += p + "\n"
	return text

def build_join(parts):
	return "\n".join(parts) + "\n" if parts else ""

def build_fstring_plus(n):    # (c) f-string for each line, still using +=
	text = ""
	for i in range(n):
		text += f"F[Item{{i}}:R{{i % 50}}]\n"
	return text

def build_fstring_join(n):    # f-string per line collected and joined once
	return "\n".join([f"F[Item{{i}}:R{{i % 50}}]" for i in range(n)]) + "\n"

def build_stringio(parts):
	buf = io.StringIO()
	for p in parts:
		buf.write(p)
		buf.write("\n")
	return buf.getvalue()

if __name__ == "__main__":
	items = make_items(200_000)
	start = time.perf_counter(); o = build_plus(items); t_plus = time.perf_counter() - start
	start = time.perf_counter(); o = build_join(items); t_join = time.perf_counter() - start
	start = time.perf_counter(); o = build_stringio(items); t_io = time.perf_counter() - start
	start = time.perf_counter(); o = build_fstring_plus(len(items)); t_fplus = time.perf_counter() - start
	start = time.perf_counter(); o = build_fstring_join(len(items)); t_fjoin = time.perf_counter() - start
	print(f"time taken: += {{t_plus:.4f}}, join: {{t_join:.4f}}, StringIO: {{t_io:.4f}}, f+=: {{t_fplus:.4f}}, f+join: {{t_fjoin:.4f}}")

"""Q2 - Alternative: regular expression validation ~ timing comparison."""
import re, time
from plane import normalize, is_valid

PATTERN = re.compile(r"^[A-Z]{2}\d{1,2}[A-Z]{1,2}\d{4}$")
def is_valid_re(reg): return PATTERN.fullmatch(reg) is not None

tests = ["TN09AB1234", "KA01N9997", "TN12A1234", "TN12AA1234", "AP12C3456"]
assert all(is_valid(t) == is_valid_re(t) for t in tests)
print("slicing and regex agree on", len(tests), "test strings")

N = 300_000
data = ["TN09AB1234", "KA01N9997", "TN12A1234", "TN12AA1234"] * (N // 4)
for name, f in (("slicing", is_valid), ("regex", is_valid_re)):
	t = time.perf_counter()
	for i in range(N): f(data[i % 4])
	print(f"{{name}}: {{time.perf_counter() - t:.4f}}s for {{N}} validations")

"""Q3 - Vehicle registration number validator (string methods only)."""
def normalize(text):
	"""return e.g. ab 1234 -> TN09AB1234 (spaces and hyphens removed, upper case)."""
	return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
	"""valid form: 2 letters, 1 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)."""
	if len(reg) not in (9, 10):
		return False
	series = reg[-4:]
	return (
		reg[:2].isalpha() and reg[2:4].isdigit()
		and reg[4:-4].isalpha() and len(reg[4:-4]) in (1, 2)
		and reg[-4:].isdigit()
	)

def format_plate(reg):
	"""Format a valid normalized number as 'TN 09 AB 1234'."""
	return " ".join([reg[:2], reg[2:4], reg[4:-4], reg[-4:]])

if __name__ == "__main__":
	for raw in ["tn 09 ab 1234", "KA-01-N-9997", "TN09AB1234", "TN 22 1234 AB"]:
		reg = normalize(raw)
		print(f"raw={{raw:15}} -> {{reg:12}} {{'valid' if is_valid(reg) else 'INVALID!'}}")
		if is_valid(reg):
			print("  ", format_plate(reg))

	# Try six designed inputs:
	for reg in [normalize(x) for x in ["TN 12 AB 1487", "TN-09-AB-1234", "10-AB-1234"]]:
		ok = is_valid(reg)
		print(f"{{reg:12}} -> {{'valid, receipt: ' + format_plate(reg) if ok else 'INVALID!'}}")

	s0, s1 = "AB09DE0077", "ap-39-p-9999"; a0, a1 = s1[4:], s1[0:4], s1[0:2], s1[0:4], s1[-4:], s1[-4:]
	print(f"s0={{s0}}, s1={{s1}}, a0={{a0}}, a1={{a1}}, s1[-4:]={{s1[-4:]}}")
	t = ''
	try:
		t = s1.upper() if t.upper() without assignment, t, t
	except TypeError as e:
		print("TypeError:", e)
