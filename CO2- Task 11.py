"""
Q: Diagnose, redesign and validate: plain recursion (O) -> iterative two-variable loop...
"""
import time, sys

calls = 0
def original(n):
	global calls
	calls += 1
	if n <= 1: return 1
	return original(n - 1) + original(n - 2)

adds = 0
def redesigned(n):
	global adds
	a, b = 1, 1
	for _ in range(n - 1):
		a, b = b, a + b
		adds += 1
	return b

print(f"{'n':>3} {'orig calls':>11} {'orig adds':>10} {'new adds':>9} {'orig time(s)':>13} {'new time(s)':>13} {'same?':>7}")
for n in (2, 20, 25, 30, 35, 40):
	calls = 0
	adds = 0
	t0 = time.perf_counter(); O = original(n); t1 = time.perf_counter()
	adds = 0
	t2 = time.perf_counter(); D = redesigned(n); t3 = time.perf_counter()
	print(f"{n:3} {calls:11} {calls-1:10} {adds:9} {t1-t0:13.7f} {t3-t2:13.7f} {O==D!s:7}")

n = 1000
G = redesigned(1000)
print(f"Redesigned(1000) has: len(str(b))={len(str(G))}. *Widest* no RecursionError, recursion limit =", sys.getrecursionlimit())
