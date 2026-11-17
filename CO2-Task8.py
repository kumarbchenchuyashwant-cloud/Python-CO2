""" Building long text: += vs join vs f-string, StringIO alternative."""
import time, io, sys

def make_items(n): return [f"Item{{i}}:R{{i % 50}}" for i in range(n)]

def build_plus(parts):
	text = ""
	for p in parts:
		text += p + "\n"
	return text

def build_join(parts):
	return "\n".join(parts) + "\n" if parts else ""

def build_fstring_plus(n):      # (c) f-string for each line, still using +=
	text = ""
	for i in range(n):
		text += f"FItem{{i}}:R{{i % 50}}\n"
	return text

def build_fstring_join(n):      # f-string per line collected and joined once
	return "\n".join([f"FItem{{i}}:R{{i % 50}}" for i in range(n)]) + "\n"

def build_stringio(parts):
	buf = io.StringIO()
	for p in parts:
		buf.write(p)
		buf.write("\n")
	return buf.getvalue()

if __name__ == "__main__":
	items = make_items(200_000)
	start = time.perf_counter(); _ = build_plus(items); plus = time.perf_counter() - start
	start = time.perf_counter(); _ = build_join(items); join = time.perf_counter() - start
	start = time.perf_counter(); _ = build_stringio(items); sio = time.perf_counter() - start
	start = time.perf_counter(); _ = build_fstring_plus(len(items)); fplus = time.perf_counter() - start
	start = time.perf_counter(); _ = build_fstring_join(len(items)); fjoin = time.perf_counter() - start
	print(f"time taken: += {{plus:.4f}}s, join: {{join:.4f}}s, StringIO: {{sio:.4f}}s, f+=: {{fplus:.4f}}s, fjoin: {{fjoin:.4f}}s, len: {{len(items)}}")
