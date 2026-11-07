"""Task 10 extension - bisection and fixed-point.

PART 1: change the constant 10 in the heat-balance equation (and show convergence speed).
PART 2: new case - break-even quantities of a small business (two roots, two brackets).
Price, demand slope and cost figures are ASSUMED.
"""
import numpy as np
from scipy.optimize import root_scalar

# ---------------- PART 1: parameter change ----------------
print("PART 1 - heat balance T - 25 - A*exp(-T/20) = 0")
for A in (10, 20, 30):
    f = lambda T, A=A: T - 25 - A*np.exp(-T/20)
    g = lambda T, A=A: 25 + A*np.exp(-T/20)
    bis = root_scalar(f, bracket=[20, 40], method="bisect", xtol=1e-10)
    T, it = 30.0, 0
    while it < 200:
        T_new = g(T); it += 1
        if abs(T_new - T) < 1e-10:
            T = T_new
            break
        T = T_new
    print(f"A={A:>2}: bisection T={bis.root:.6f} ({bis.iterations} halvings) | fixed-point T={T:.6f} ({it} iterations)")
print()

# ---------------- PART 2: new case ----------------
# Price falls as quantity rises: price = P0 - 0.02*q. Cost = 2000 + 30q + 0.01q^2.
def profit(q, P0=100.0):
    revenue = q * (P0 - 0.02*q)
    cost = 2000 + 30*q + 0.01*q**2
    return revenue - cost


print("PART 2 - break-even points (profit = 0)")
for P0 in (100.0, 90.0):
    low = root_scalar(profit, args=(P0,), bracket=[0, 100], method="bisect", xtol=1e-8)
    high = root_scalar(profit, args=(P0,), bracket=[1000, 3000], method="bisect", xtol=1e-8)
    q_best = (P0 - 30) / 0.06           # where d(profit)/dq = 0
    print(f"Base price {P0:.0f}: profitable between q={low.root:.1f} and q={high.root:.1f} units; "
          f"best volume ~{q_best:.0f} units with profit {profit(q_best, P0):,.0f}")
