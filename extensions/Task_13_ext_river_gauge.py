"""Task 13 extension - interpolation.

PART 1: change the evaluation time (inside and outside the data range).
PART 2: new case - a river-level gauge logs every 3 hours; fill a missing reading and
        test which method does better by hiding each known value in turn.
Water levels are ASSUMED / illustrative.
"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline

# ---------------- PART 1: parameter change ----------------
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temp = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
lin, cub = interp1d(hours, temp), CubicSpline(hours, temp)

print("PART 1 - different query times")
for t in (9.5, 10.5, 13.75):
    print(f"t={t}: linear={float(lin(t)):.3f} C, cubic={float(cub(t)):.3f} C")
try:
    lin(14.5)
except ValueError as err:
    print("Linear at 14.5 h (outside data) ->", "ValueError:", str(err)[:60])
print(f"Cubic spline at 14.5 h (extrapolation, unreliable): {float(cub(14.5)):.3f} C")
print()

# ---------------- PART 2: new case ----------------
t = np.arange(0, 27, 3, dtype=float)       # 0,3,...,24 h
level = np.array([1.20, 1.18, 1.25, 1.60, 2.10, 2.35, 2.05, 1.55, 1.30])  # metres

print("PART 2 - leave-one-out test on river level (m)")
print(f"{'time':>5} {'actual':>7} {'linear':>7} {'cubic':>7} {'lin err':>8} {'cub err':>8}")
lin_err, cub_err = [], []
for k in range(1, len(t) - 1):
    mask = np.arange(len(t)) != k
    est_l = float(interp1d(t[mask], level[mask])(t[k]))
    est_c = float(CubicSpline(t[mask], level[mask])(t[k]))
    lin_err.append(abs(est_l - level[k])); cub_err.append(abs(est_c - level[k]))
    print(f"{t[k]:>5.0f} {level[k]:>7.2f} {est_l:>7.3f} {est_c:>7.3f} {lin_err[-1]:>8.3f} {cub_err[-1]:>8.3f}")
print(f"Mean absolute error: linear={np.mean(lin_err):.3f} m, cubic={np.mean(cub_err):.3f} m")

mask = t != 15
est = float(CubicSpline(t[mask], level[mask])(15.0))
print(f"If the 15:00 reading is lost, cubic spline estimates {est:.2f} m (true {level[t==15][0]:.2f} m): "
      "peaks are the hardest points to recover.")
