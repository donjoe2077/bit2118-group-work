"""Task 19 extension - optimization.

PART 1: change the cost of a Type A server (12 -> 8) and see the plan switch.
PART 2: new case - cheapest fence for a rectangular farm plot of 500 m^2 with one side
        along a river (no fence needed there). Area is ASSUMED; analytic answer is known.
"""
import numpy as np
from scipy.optimize import minimize

# ---------------- PART 1: parameter change ----------------
print("PART 1 - cloud cost optimisation, Type A unit cost varies (Type B = 18)")
for cost_a in (12, 8):
    sol = minimize(lambda z: cost_a*z[0] + 18*z[1], x0=[5, 3], method="SLSQP",
                   bounds=[(0, None), (0, None)],
                   constraints={"type": "ineq", "fun": lambda z: 100*z[0] + 170*z[1] - 1000})
    best = min(((cost_a*a + 18*b, a, b, 100*a + 170*b)
                for a in range(20) for b in range(20) if 100*a + 170*b >= 1000))
    print(f"A costs {cost_a:>2}: A={sol.x[0]:.3f}, B={sol.x[1]:.3f}, cost={sol.fun:.2f} | "
          f"whole servers (cost, A, B, capacity)={best}")
print("Cost per unit of capacity: A = %.4f, B = %.4f -> the cheaper ratio wins." % (12/100, 18/170))
print("At A=8 the ratio is 0.0800 < 0.1059, so the plan switches entirely to Type A.")
print()

# ---------------- PART 2: new case ----------------
# x = side perpendicular to the river (two of these), y = side parallel to the river (one)
fence = lambda z: 2*z[0] + z[1]
area = {"type": "eq", "fun": lambda z: z[0]*z[1] - 500.0}
sol = minimize(fence, x0=[10.0, 50.0], method="SLSQP", bounds=[(1, None), (1, None)], constraints=area)
x, y = sol.x
print("PART 2 - fenced farm plot, area 500 m^2, river on one side")
print(f"Optimizer: x={x:.3f} m, y={y:.3f} m, fence length={sol.fun:.3f} m, converged={sol.success}")
print(f"Analytic : x=sqrt(250)={np.sqrt(250):.3f} m, y=2x={2*np.sqrt(250):.3f} m, length=4*sqrt(250)={4*np.sqrt(250):.3f} m")
print(f"A naive 10 m x 50 m plot needs {fence([10, 50]):.0f} m of fence ({fence([10,50])/sol.fun-1:.1%} more).")
