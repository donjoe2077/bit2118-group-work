"""Task 06 extension - systems of linear equations.

PART 1: change the observed totals of the server problem (and show a singular case).
PART 2: new case - mesh-current analysis of a three-loop resistor circuit.
Resistor and voltage values are ASSUMED.
"""
import numpy as np

# ---------------- PART 1: parameter change ----------------
A = np.array([[4., 2.], [8., 12.]])
print("PART 1 - server problem with new totals")
for b in ([20., 72.], [22., 80.]):
    x = np.linalg.solve(A, np.array(b))
    print(f"b={b}: A={x[0]:.3f}, B={x[1]:.3f}")
print("The second answer is not whole numbers, so those totals cannot come from whole servers.")

singular = np.array([[4., 2.], [8., 4.]])   # row 2 = 2 x row 1
print("det of dependent system:", np.linalg.det(singular))
try:
    np.linalg.solve(singular, np.array([20., 40.]))
except np.linalg.LinAlgError as err:
    print("Singular system ->", err)
print()

# ---------------- PART 2: new case ----------------
R1, R2, R3, R4, R5 = 10., 20., 30., 15., 25.   # ohms
V1, V2 = 12., 6.                                # volts

# Kirchhoff's voltage law for mesh currents I1, I2, I3 (amps)
M = np.array([
    [R1 + R4,      -R4,        0.0],
    [-R4,    R4 + R2 + R5,    -R5],
    [0.0,         -R5,    R5 + R3],
])
v = np.array([V1, 0.0, -V2])

I = np.linalg.solve(M, v)
print("PART 2 - mesh currents")
for k, cur in enumerate(I, start=1):
    print(f"I{k} = {cur*1000:.3f} mA")
print("Residual norm:", np.linalg.norm(v - M @ I))
print(f"Current through shared resistor R4 (I1-I2): {(I[0]-I[1])*1000:.3f} mA")
print(f"Current through shared resistor R5 (I2-I3): {(I[1]-I[2])*1000:.3f} mA")
print(f"Condition number of the matrix: {np.linalg.cond(M):.2f} (small = well-behaved)")
