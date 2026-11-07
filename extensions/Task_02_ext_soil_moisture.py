"""Task 02 extension - NumPy arrays.

PART 1: change one input of the original program (add a +3 C sensor offset).
PART 2: new real-world case - greenhouse soil-moisture sensor (24 hourly readings).

All data below are ASSUMED / illustrative values, not measurements.
"""
import numpy as np

# ---------------- PART 1: parameter change ----------------
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])
shifted = temperatures_c + 3.0   # the sensor is re-mounted in a sunnier spot
print("PART 1 - original vs +3 C offset")
print(f"Mean: {temperatures_c.mean():.2f} C -> {shifted.mean():.2f} C")
print(f"Min : {temperatures_c.min():.2f} C -> {shifted.min():.2f} C")
print(f"Max : {temperatures_c.max():.2f} C -> {shifted.max():.2f} C")
print(f"Std dev (spread) unchanged: {temperatures_c.std():.3f} vs {shifted.std():.3f}")
print()

# ---------------- PART 2: new case ----------------
# Volumetric soil moisture (%) every hour; irrigation happens at hour 6.
moisture = np.array([
    34, 33, 33, 32, 31, 30,
    45, 44, 42, 40, 38, 36,
    34, 33, 31, 30, 29, 28,
    27, 27, 26, 26, 25, 25
], dtype=float)
threshold = 30.0                      # crops are stressed below this value

below = moisture < threshold          # boolean mask, one test for all values
hours = np.arange(24)

print("PART 2 - soil moisture")
print(f"Mean moisture: {moisture.mean():.2f} %")
print(f"Min / Max: {moisture.min():.0f} % / {moisture.max():.0f} %")
print(f"Hours below {threshold:.0f} %: {below.sum()}")
print("Stressed hours:", hours[below].tolist())
print(f"Fraction of day stressed: {below.mean():.1%}")
# Normalised 0-1 scale applied to the entire array at once
normalised = (moisture - moisture.min()) / (moisture.max() - moisture.min())
print("First six normalised values:", np.round(normalised[:6], 3))
