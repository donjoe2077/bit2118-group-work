"""Task 07 extension - LU decomposition.

PART 1: change the measurement vector (scale it) and see the solution scale.
PART 2: new case - implicit (backward Euler) heat conduction in a metal rod where the
        same matrix is used at every time step, so LU factors are reused.
Rod size, diffusion number and starting temperatures are ASSUMED.
"""
import timeit
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# ---------------- PART 1: parameter change ----------------
A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
lu, piv = lu_factor(A)
b = np.array([16., 11., 9.])
print("PART 1 - linearity of Ax=b")
print("x for b       :", np.round(lu_solve((lu, piv), b), 4))
print("x for 2*b     :", np.round(lu_solve((lu, piv), 2*b), 4), "(exactly double)")
print("x for b + b2  :", np.round(lu_solve((lu, piv), b + np.array([1., 1., 1.])), 4))
print()

# ---------------- PART 2: new case ----------------
n = 300             # interior points along the rod
r = 1.0             # r = alpha*dt/dx^2 (diffusion number)
steps = 300

L = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
M = np.eye(n) + r*L                     # (I + r L) u_new = u_old, ends held at 0 C

u0 = np.zeros(n)
u0[140:160] = 100.0                     # a hot 20-point section in the middle


def march_with_solve():
    u = u0.copy()
    for _ in range(steps):
        u = np.linalg.solve(M, u)
    return u


def march_with_lu():
    f = lu_factor(M)                    # factor ONCE
    u = u0.copy()
    for _ in range(steps):
        u = lu_solve(f, u)
    return u


t_solve = timeit.timeit(march_with_solve, number=1)
t_lu = timeit.timeit(march_with_lu, number=1)
u_a, u_b = march_with_solve(), march_with_lu()

print("PART 2 - heat in a rod, 300 nodes x 300 time steps")
print("Same answer from both methods:", np.allclose(u_a, u_b))
print(f"Peak temperature: {u0.max():.1f} C -> {u_b.max():.2f} C after {steps} steps")
print(f"Total heat (sum of temps): {u0.sum():.1f} -> {u_b.sum():.1f} "
      "(unchanged: the spreading heat has not yet reached the cold ends)")
print(f"Hot region after {steps} steps spans {(u_b > 1.0).sum()} nodes (was 20)")
print(f"np.linalg.solve every step: {t_solve:.3f} s | LU factor once: {t_lu:.3f} s | speed-up ~{t_solve/t_lu:.1f}x")
