"""Task 12 extension - nonlinear systems.

PART 1: change the circle radius in the circle/parabola problem (including a radius with no solution).
PART 2: new case - locate a phone that is 5 km from tower 1 and 4 km from tower 2
        (two circles). Tower positions and ranges are ASSUMED.
"""
import numpy as np
from scipy.optimize import root

# ---------------- PART 1: parameter change ----------------
print("PART 1 - circle x^2+y^2=r^2 and parabola y=x^2-1")
for r in (2.0, 3.0, 0.5):
    def eq(z, r=r):
        x, y = z
        return [x**2 + y**2 - r**2, y - (x**2 - 1)]
    sol = root(eq, [1.0, 1.0])
    print(f"r={r}: x={sol.x[0]:.4f}, y={sol.x[1]:.4f}, "
          f"residual norm={np.linalg.norm(eq(sol.x)):.2e}, converged={sol.success}")
print("(For r < sqrt(3)/2 = 0.866 the curves never meet, so the solver cannot reach zero residuals.)")
print()

# ---------------- PART 2: new case ----------------
T1, R1 = np.array([0.0, 0.0]), 5.0
T2, R2 = np.array([6.0, 0.0]), 4.0


def towers(z):
    return [np.sum((z - T1)**2) - R1**2,
            np.sum((z - T2)**2) - R2**2]


print("PART 2 - two-tower position fix")
for guess in ([3.0, 3.0], [3.0, -3.0]):
    sol = root(towers, guess)
    print(f"Guess {guess}: position=({sol.x[0]:.4f}, {sol.x[1]:.4f}) km, "
          f"residuals={np.round(towers(sol.x), 10)}, converged={sol.success}")

x = (R1**2 - R2**2 + 6.0**2) / (2*6.0)
y = np.sqrt(R1**2 - x**2)
print(f"Algebra check: x={x:.4f}, y=+-{y:.4f}")
print("Two towers give two possible positions; a third tower or a compass heading picks the right one.")
