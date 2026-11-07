"""Task 18 extension - solve_ivp.

PART 1: change the capacitance (and resistance) in the RC circuit.
PART 2: new case - a mass-spring-damper (vehicle suspension) written as two first-order ODEs.
Mass, spring constant and damping values are ASSUMED.
"""
import numpy as np
from scipy.integrate import solve_ivp

# ---------------- PART 1: parameter change ----------------
Vs = 5.0
print("PART 1 - RC charging, voltage after 1 s")
for R, C in ((1000, 0.001), (1000, 0.002), (500, 0.001)):
    sol = solve_ivp(lambda t, V: [(Vs - V[0])/(R*C)], (0, 1), [0.0],
                    rtol=1e-9, atol=1e-11, t_eval=[1.0])
    exact = Vs*(1 - np.exp(-1.0/(R*C)))
    print(f"R={R:>4} ohm, C={C*1000:.0f} mF, time constant={R*C:.1f} s: "
          f"V(1s)={sol.y[0,0]:.4f} V (exact {exact:.4f})")
print()

# ---------------- PART 2: new case ----------------
m, k = 1.0, 25.0                      # natural frequency = sqrt(k/m) = 5 rad/s


def make(c):
    def f(t, y):
        x, v = y
        return [v, -(c*v + k*x)/m]    # m x'' + c x' + k x = 0
    return f


t_eval = np.linspace(0, 6, 1201)
print("PART 2 - suspension after a 0.10 m bump (starts at x=0.10 m, v=0)")
for c, label in ((1.0, "light damping"), (10.0, "critical damping"), (14.0, "heavy damping")):
    sol = solve_ivp(make(c), (0, 6), [0.10, 0.0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
    x = sol.y[0]
    zeta = c / (2*np.sqrt(m*k))
    undershoot = max(0.0, -x.min())
    outside = np.where(np.abs(x) > 0.005)[0]      # 5 percent of the bump
    settle = sol.t[outside[-1]] if outside.size else 0.0
    print(f"c={c:>4} ({label:>16}, damping ratio {zeta:.2f}): "
          f"overshoot below zero={undershoot*100:5.2f} cm, settles within 0.5 cm after {settle:4.2f} s")
