"""Task 03 extension - vectorization.

PART 1: change the data size N and watch the speed-up.
PART 2: new case - fees and currency conversion for mobile-money style transactions.
Transaction amounts and the exchange rate are SIMULATED / ASSUMED.
"""
import timeit
import numpy as np

rng = np.random.default_rng(42)

# ---------------- PART 1: parameter change (N) ----------------
print("PART 1 - speed-up versus number of values")
for n in (1_000, 100_000, 1_000_000):
    data = rng.uniform(5, 250, n)

    def loop():
        out = []
        for v in data:
            out.append((v / 1000.0) ** 2)
        return out

    def vec():
        return (data / 1000.0) ** 2

    t_loop = timeit.timeit(loop, number=1)
    t_vec = timeit.timeit(vec, number=5) / 5
    print(f"N={n:>9,}: loop={t_loop:.5f}s  vectorized={t_vec:.6f}s  speed-up={t_loop/t_vec:.0f}x")
print()

# ---------------- PART 2: new case ----------------
# 1,000,000 transactions in KES. Fee = 1% of amount, but at least 5 and at most 100.
# Customer receives amount minus fee; report the net amount in USD (assumed rate 129 KES/USD).
N = 1_000_000
amount_kes = rng.lognormal(mean=6.5, sigma=1.0, size=N).round(2)
RATE = 129.0
MIN_FEE, MAX_FEE = 5.0, 100.0


def loop_version():
    net = []
    for a in amount_kes:
        fee = 0.01 * a
        if fee < MIN_FEE:
            fee = MIN_FEE
        elif fee > MAX_FEE:
            fee = MAX_FEE
        net.append((a - fee) / RATE)
    return net


def vector_version():
    fee = np.clip(0.01 * amount_kes, MIN_FEE, MAX_FEE)
    return (amount_kes - fee) / RATE


t_loop = timeit.timeit(loop_version, number=1)
t_vec = timeit.timeit(vector_version, number=3) / 3
same = np.allclose(loop_version(), vector_version())

fees = np.clip(0.01 * amount_kes, MIN_FEE, MAX_FEE)
print("PART 2 - transactions")
print(f"Results identical: {same}")
print(f"Total fees collected: {fees.sum():,.0f} KES")
print(f"Average fee: {fees.mean():.2f} KES ({(fees.sum()/amount_kes.sum()):.2%} of money moved)")
print(f"Transactions hitting the fee cap: {(fees == MAX_FEE).sum():,}")
print(f"Loop time: {t_loop:.4f} s | Vectorized: {t_vec:.4f} s | Speed-up: {t_loop/t_vec:.0f}x")
