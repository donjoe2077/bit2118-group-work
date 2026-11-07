"""Task 15 extension - numerical differentiation.

PART 1: change the step size h and compare forward and central differences on sin(x).
PART 2: new case - acceleration of a car from speed readings taken every 2 s.
Speed readings are ASSUMED.
"""
import numpy as np

# ---------------- PART 1: parameter change ----------------
x0 = 1.0
exact = np.cos(x0)
print("PART 1 - derivative of sin(x) at x=1 (exact = cos(1) = %.8f)" % exact)
print(f"{'h':>8} {'forward err':>13} {'central err':>13}")
for h in (0.1, 0.01, 0.001, 1e-6, 1e-12):
    fwd = (np.sin(x0 + h) - np.sin(x0)) / h
    cen = (np.sin(x0 + h) - np.sin(x0 - h)) / (2*h)
    print(f"{h:>8.0e} {abs(fwd-exact):>13.3e} {abs(cen-exact):>13.3e}")
print("Error shrinks with h until round-off takes over (h=1e-12).")
print()

# ---------------- PART 2: new case ----------------
t = np.array([0, 2, 4, 6, 8, 10], dtype=float)                 # seconds
speed_kmh = np.array([0, 18, 35, 50, 60, 65], dtype=float)
v = speed_kmh / 3.6                                             # m/s

accel = np.gradient(v, t, edge_order=2)                         # central inside, 2nd-order at ends
print("PART 2 - acceleration from speed")
for ti, vi, ai in zip(t, v, accel):
    print(f"t={ti:>4.0f}s speed={vi:6.2f} m/s acceleration={ai:5.2f} m/s^2")
print(f"Peak acceleration: {accel.max():.2f} m/s^2 at t={t[accel.argmax()]:.0f} s")
print(f"Distance covered (trapezoid on speed): {np.trapezoid(v, t):.1f} m")
