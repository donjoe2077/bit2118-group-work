"""Task 04 extension - floating-point errors.

PART 1: change the comparison tolerance, and push the unstable formula to x = 1e-16.
PART 2: new case - accumulated round-off when adding a small amount many times
        (e.g. a system that adds 0.1 to a running total a million times).
"""
import math
import numpy as np

# ---------------- PART 1: parameter change ----------------
a, b = 0.1 + 0.2, 0.3
print("PART 1 - tolerance matters")
print("rtol=0, atol=1e-17 :", np.isclose(a, b, rtol=0, atol=1e-17))
print("rtol=0, atol=1e-9  :", np.isclose(a, b, rtol=0, atol=1e-9))
print("default tolerances :", np.isclose(a, b))
print(f"Actual difference |a-b| = {abs(a-b):.3e}")
print()
for x in (1e-12, 1e-14, 1e-16):
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}  stable={stable:.12f}")
print()

# ---------------- PART 2: new case ----------------
N = 1_000_000
true_total = 100_000.0          # 0.1 * 1,000,000

naive = 0.0
for _ in range(N):
    naive += 0.1

acc32 = np.float32(0.0)
step32 = np.float32(0.1)
for _ in range(N):
    acc32 += step32

pairwise = np.sum(np.full(N, 0.1))
exact_sum = math.fsum([0.1] * N)

print("PART 2 - adding 0.1 one million times (true total = 100000)")
print(f"float64 running loop : {naive:.10f}  abs error {abs(naive-true_total):.3e}")
print(f"float32 running loop : {float(acc32):.4f}  abs error {abs(float(acc32)-true_total):.3e}")
print(f"np.sum (pairwise)    : {pairwise:.10f}  abs error {abs(pairwise-true_total):.3e}")
print(f"math.fsum (exact)    : {exact_sum:.10f}  abs error {abs(exact_sum-true_total):.3e}")
print(f"float32 relative error: {abs(float(acc32)-true_total)/true_total:.4%}")
