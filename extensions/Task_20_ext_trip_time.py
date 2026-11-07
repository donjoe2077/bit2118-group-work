"""Task 20 extension - Monte Carlo.

PART 1: change N and capacity in the server-overload simulation and compare to the exact value.
PART 2: new case - probability that a three-leg bus journey takes longer than 90 minutes.
Leg-time distributions are ASSUMED.
"""
import numpy as np
from scipy.stats import norm

rng = np.random.default_rng(42)

# ---------------- PART 1: parameter change ----------------
print("PART 1 - overload probability, demand ~ Normal(850, 120)")
for capacity in (1000.0, 1100.0):
    exact = norm.sf(capacity, loc=850, scale=120)
    print(f"capacity {capacity:.0f}: exact probability = {exact:.4%}")
    for N in (100, 10_000, 1_000_000):
        p = (rng.normal(850, 120, N) > capacity).mean()
        se = np.sqrt(max(p*(1 - p), 1e-12) / N)
        print(f"   N={N:>9,}: estimate={p:7.3%} +- {se:.3%} (error vs exact {abs(p-exact):.3%})")
print()

# ---------------- PART 2: new case ----------------
LIMIT = 90.0
print(f"PART 2 - probability a journey takes more than {LIMIT:.0f} min")
for N in (1_000, 100_000, 1_000_000):
    leg1 = rng.triangular(20, 25, 40, N)                    # town to highway
    leg2 = rng.triangular(15, 20, 35, N)                    # highway section
    leg3 = np.maximum(rng.normal(30, 5, N), 0.0)            # city centre approach
    total = leg1 + leg2 + leg3
    p = (total > LIMIT).mean()
    se = np.sqrt(p*(1 - p)/N)
    print(f"N={N:>9,}: P(total > {LIMIT:.0f})={p:.3%} +- {se:.3%} | mean trip={total.mean():.1f} min, "
          f"95th percentile={np.percentile(total, 95):.1f} min")
