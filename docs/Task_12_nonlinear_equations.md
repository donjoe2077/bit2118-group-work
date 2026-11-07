# Task 12 – Polynomial and Nonlinear Equation Solving

**Concept:** find values that make every equation's residual zero.
**Code:** `code/Task_12_nonlinear_equations.py` · **Extension:** `extensions/Task_12_ext_two_towers.py`

## B. Inputs and mathematical operations
- **Inputs:** circle x² + y² = 4, parabola y = x² − 1, initial guesses (1, 1) and (−1, 1).
- **Operation:** `scipy.optimize.root` iterates until both residuals are near zero; residuals are printed to verify.

## Output of the original program
```
Initial guess: [1.0, 1.0]    Intersection: [1.51748991 1.30277564]   Converged: True
Initial guess: [-1.0, 1.0]   Intersection: [-1.51748991 1.30277564]  Converged: True
(residuals about 2e-13)
```

## C. Changing an input
Circle radius changed (r² in the first equation):
- r = 3: intersection (1.8364, 2.3723), converged.
- r = 0.5: the solver stops at (0.50, −0.50) with residual norm 0.354 and `converged=False`. Substituting x² = y + 1 gives y² + y + 1 = r², which has real solutions only for r ≥ √3/2 ≈ 0.866, so a circle that small never touches the parabola.

## D. Interpretation
There are two intersection points, mirror images across the y-axis, because the parabola and circle are symmetric. Starting on the left or right of the axis decides which one the solver finds. Always check the converged flag and the residuals: a returned number is not necessarily a solution.

## E. New case – locating a phone from two towers
- **Assumptions:** tower 1 at (0, 0) with range 5 km, tower 2 at (6, 0) with range 4 km.
- **Output:** positions (3.7500, 3.3072) km and (3.7500, −3.3072) km, residuals 0; algebra gives the same x = 3.75 and y = ±3.3072.
- **Interpretation:** two circles meet at two points, so two ranges alone cannot say which side the phone is on. A third tower or a direction reading removes the ambiguity, which is the idea behind GPS-style positioning.
