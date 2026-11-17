"""
Alternative concepts: match-case and a (limit, decision) table search.
"""
import time, sys

def by_elif(units):
	if units < 100: return "FULL"
	elif units < 200: return "PARTIAL"
	else: return "NONE"

def by_match(units):
	match units:
		case u if u < 100: return "FULL"
		case u if u < 200: return "PARTIAL"
		case _: return "NONE"

SLABS = [(100, "FULL"), (200, "PARTIAL")]
def by_table(units):
	for limit, decision in SLABS:
		if units < limit:
			return decision
	return "NONE"

assert all(by_elif(u) == by_match(u) == by_table(u) for u in range(0, 400))
print("All three versions agree for 0..399 units")

N = 1_000_000
for fn in (by_elif, by_match, by_table):
	t1 = time.perf_counter()
	for i in range(N):
		fn(i % 400)
	t2 = time.perf_counter()
	print(f"{fn.__name__:<10} {time.perf_counter() - t1:.3f} s for {N} decisions")

print(f"Python {sys.version_info.major}.{sys.version_info.minor} on {sys.platform}")
