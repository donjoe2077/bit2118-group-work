"""Task 08 extension - iterative methods.

PART 1: change tolerance and boundary temperature in the 5-point model.
PART 2: new case - longer rods (more grid points) to see how iteration counts grow.
Boundary temperatures (100 C and 20 C) are ASSUMED.
"""
import numpy as np


def jacobi(A, b, tol=1e-8, max_iter=200000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    for k in range(1, max_iter + 1):
        x_new = (b - R @ x) / D
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k
        x = x_new
    return x, max_iter


def gauss_seidel(A, b, tol=1e-8, max_iter=200000):
    x = np.zeros_like(b)
    for k in range(1, max_iter + 1):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        if np.linalg.norm(x - old, ord=np.inf) < tol:
            return x, k
    return x, max_iter


def rod(n, left=100.0, right=20.0):
    A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    b = np.zeros(n)
    b[0], b[-1] = left, right
    return A, b


# ---------------- PART 1: parameter change ----------------
print("PART 1 - tolerance and boundary change on the 5-point rod")
A, b = rod(5)
for tol in (1e-4, 1e-8, 1e-12):
    _, kj = jacobi(A, b, tol)
    xg, kg = gauss_seidel(A, b, tol)
    err = np.max(np.abs(xg - np.linalg.solve(A, b)))
    print(f"tol={tol:.0e}: Jacobi {kj:>3} it | Gauss-Seidel {kg:>3} it | GS max error {err:.2e}")
A, b = rod(5, left=80.0, right=20.0)
print("Left boundary 80 C ->", np.round(np.linalg.solve(A, b), 3))
print()

# ---------------- PART 2: new case ----------------
print("PART 2 - iterations needed (tol=1e-8) as the rod gets longer")
print(f"{'n':>4} {'Jacobi':>8} {'Gauss-Seidel':>13} {'max error (GS)':>15}")
for n in (5, 10, 20, 40):
    A, b = rod(n)
    xj, kj = jacobi(A, b)
    xg, kg = gauss_seidel(A, b)
    err = np.max(np.abs(xg - np.linalg.solve(A, b)))
    print(f"{n:>4} {kj:>8} {kg:>13} {err:>15.2e}")
