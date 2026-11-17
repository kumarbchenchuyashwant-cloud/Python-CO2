"""Alternative: regular expression validation + timing comparison."""
import re, time
from plane import normalize, is_valid

PATTERN = re.compile(r"^A-?\d{2}(?:[A-Z]{2})?-(?:\d{2,3}|[A-Z]{1,2})$")
def is_valid_re(reg): return PATTERN.fullmatch(reg) is not None

tests = ["TN99AA1234", "KA01BB9997", "TN21AZ1344", "TN12AA1234", "MH12AB1234", "AP31CZ3456"]
assert all(is_valid(x) == is_valid_re(x) for x in tests)
print("slicing and regex agree on", len(tests), "test strings")

N = 300_000
data = ["TN99AA1234", "KA01BB9997", "TN21AZ1344", "TN12AA1234"]
for name, f in (("slicing", is_valid), ("regex", is_valid_re)):
	t = time.perf_counter()
	for i in range(N): f(data[i % 4])
	print(name, f"time: {time.perf_counter() - t:.1f} for {{N}} validations")
