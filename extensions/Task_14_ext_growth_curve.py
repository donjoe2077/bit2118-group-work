"""Task 14 extension - curve fitting.

PART 1: change the model degree for the server data (linear / quadratic / cubic).
PART 2: new case - plant height over time fitted with a logistic growth curve.
The plant data are SYNTHETIC (generated from a logistic curve plus noise, seed 7).
"""
import numpy as np
from scipy.optimize import curve_fit

# ---------------- PART 1: parameter change ----------------
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
resp = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

print("PART 1 - polynomial degree")
for deg in (1, 2, 3):
    coef = np.polyfit(users, resp, deg)
    rmse = np.sqrt(np.mean((resp - np.polyval(coef, users))**2))
    print(f"degree {deg}: RMSE={rmse:6.2f} ms | prediction at 400 users={np.polyval(coef, 400):7.1f} ms")
print()

# ---------------- PART 2: new case ----------------
rng = np.random.default_rng(7)
days = np.arange(0, 41, 5, dtype=float)
height = 120/(1 + np.exp(-0.18*(days - 20))) + rng.normal(0, 2.0, days.size)


def logistic(t, L, k, t0):
    return L/(1 + np.exp(-k*(t - t0)))


def exponential(t, a, k):
    return a*np.exp(k*t)


pl, _ = curve_fit(logistic, days, height, p0=[100, 0.1, 15])
pe, _ = curve_fit(exponential, days, height, p0=[5, 0.05], maxfev=10000)
rm_l = np.sqrt(np.mean((height - logistic(days, *pl))**2))
rm_e = np.sqrt(np.mean((height - exponential(days, *pe))**2))

print("PART 2 - plant growth (cm)")
print("Days  :", days.astype(int).tolist())
print("Height:", np.round(height, 1).tolist())
print(f"Logistic fit : max height L={pl[0]:.1f} cm, rate k={pl[1]:.3f}/day, midpoint day {pl[2]:.1f}, RMSE={rm_l:.2f} cm")
print(f"Exponential  : a={pe[0]:.2f}, k={pe[1]:.3f}/day, RMSE={rm_e:.2f} cm")
for d in (50, 60):
    print(f"Day {d}: logistic predicts {logistic(d, *pl):.1f} cm | exponential predicts {exponential(d, *pe):.0f} cm")
