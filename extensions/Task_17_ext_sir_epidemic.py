"""Task 17 extension - Euler method.

PART 1: change the step size h in the cooling problem.
PART 2: new case - a simple SIR epidemic model solved by Euler's method.
Population, beta and gamma are ASSUMED (illustrative, not a real disease).
"""
import numpy as np

# ---------------- PART 1: parameter change ----------------
T_amb, T0, k = 25.0, 90.0, 0.12
exact_30 = T_amb + (T0 - T_amb)*np.exp(-k*30)
print(f"PART 1 - cooling after 30 min (exact {exact_30:.4f} C)")
for h in (5.0, 2.0, 1.0, 0.1):
    T = T0
    for _ in range(int(round(30/h))):
        T += h * (-k*(T - T_amb))
    print(f"h={h:>4}: Euler={T:8.4f} C, error={abs(T-exact_30):.4f} C")
print()

# ---------------- PART 2: new case ----------------
N, beta, gamma = 1000.0, 0.30, 0.10          # R0 = beta/gamma = 3
print(f"PART 2 - SIR model (population {N:.0f}, beta={beta}, gamma={gamma}, R0={beta/gamma:.1f})")
for h in (1.0, 0.1):
    S, I, R = N - 1.0, 1.0, 0.0
    peak_I, peak_day = I, 0.0
    steps = int(160/h)
    for s in range(1, steps + 1):
        infection = beta*S*I/N
        recovery = gamma*I
        S, I, R = S - h*infection, I + h*(infection - recovery), R + h*recovery
        if I > peak_I:
            peak_I, peak_day = I, s*h
    print(f"h={h:>3}: peak infected={peak_I:6.1f} on day {peak_day:5.1f}, "
          f"never-infected at day 160={S:6.1f}, recovered={R:6.1f}")

beta2 = 0.15                                  # interventions halve the contact rate (R0=1.5)
S, I, R = N - 1.0, 1.0, 0.0
peak2 = I
for s in range(160):
    infection = beta2*S*I/N
    recovery = gamma*I
    S, I, R = S - infection, I + infection - recovery, R + recovery
    peak2 = max(peak2, I)
print(f"With beta={beta2} (R0=1.5): peak infected={peak2:.1f}, total ever infected by day 160={N-S:.0f}")
