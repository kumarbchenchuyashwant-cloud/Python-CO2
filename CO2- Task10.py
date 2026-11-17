""" Counting ways to climb n temple steps (1 or 2 at a time)."""
from functools import lru_cache
import sys

calls = 0

def ways_naive(n):
	"""Ways to climb n temple steps taking 1 or 2 steps at a time."""
	global calls
	calls += 1
	if n <= 1:
		return 1
	return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
	global calls
	calls += 1
	if n <= 1:
		return 1
	return ways_memo(n - 1) + ways_memo(n - 2)

def ways_loop(n):
	a, b = 1, 1
	for _ in range(n - 1):
		a, b = b, a + b
	return b if n >= 1 else 1

if __name__ == "__main__":
	calls = 0; print("naive:", ways_naive(25), "calls =", calls)
	calls = 0; print("memo :", ways_memo(25), "calls =", calls)
	print("recursion_limit =", sys.getrecursionlimit())
	try:
		calls = 0; ways_memo.cache_clear(); ways_memo(1000)
	except RecursionError as e:
		print("RecursionError:", e)
