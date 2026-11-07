"""Task 16 extension - numerical integration.

PART 1: change the number of smart-meter samples by interpolating a smooth daily curve.
PART 2: new case - total rainfall from a storm intensity record.
Intensity r(t) = 12*t*exp(-t/1.5) mm/h for 0 <= t <= 6 h is ASSUMED (rain builds quickly
then fades), so the exact total is known and we can measure the error of each rule.
"""
import numpy as np
from scipy.integrate import simpson

# ---------------- PART 1: parameter change ----------------
# A smooth "true" power curve (kW) over 12 hours, sampled 7 and 13 times.
def power(t):
    return 1.0 + 0.8*np.sin(np.pi*t/12)

exact_energy = 12.0 + 0.8*(24/np.pi)      # integral of the curve over 0..12
print(f"PART 1 - exact energy = {exact_energy:.5f} kWh")
for n in (4, 7, 13):
    t = np.linspace(0, 12, n)
    trap = np.trapezoid(power(t), t)
    simp = simpson(power(t), x=t)
    print(f"{n:>2} samples: trapezoid={trap:.5f} (err {abs(trap-exact_energy):.1e}) | "
          f"Simpson={simp:.5f} (err {abs(simp-exact_energy):.1e})")
print()

# ---------------- PART 2: new case ----------------
def rain(t):
    return 12*t*np.exp(-t/1.5)


a, T = 1.5, 6.0
exact_rain = 12*a**2*(1 - np.exp(-T/a)*(1 + T/a))      # analytic integral

print(f"PART 2 - rainfall total (exact = {exact_rain:.4f} mm)")
for n in (4, 7, 13, 25):
    t = np.linspace(0, 6, n)
    trap = np.trapezoid(rain(t), t)
    simp = simpson(rain(t), x=t)
    print(f"{n:>2} readings: trapezoid={trap:7.4f} mm (err {abs(trap-exact_rain):.2e}) | "
          f"Simpson={simp:7.4f} mm (err {abs(simp-exact_rain):.2e})")
print("More frequent readings shrink the error; Simpson improves much faster than the trapezoid rule.")
