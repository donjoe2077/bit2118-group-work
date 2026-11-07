# Task 07 – Gaussian Elimination and LU Decomposition

**Concept:** factor A once (PA = LU) and reuse the factors for many right-hand sides.
**Code:** `code/Task_07_gaussian_lu.py` · **Extension:** `extensions/Task_07_ext_heat_rod_lu.py`

## B. Inputs and mathematical operations
- **Inputs:** a fixed 3×3 matrix A and three measurement vectors b.
- **Operations:** `lu_factor(A)` once, then `lu_solve` for each b, with the residual b − A x for checking.

## Output of the original program
```
Measurement set 1  Solution: [5. 5. 5.]                       Residual norm: 0.0
Measurement set 2  Solution: [5.31707317 5.26829268 4.75609756]  Residual norm: 1.78e-15
Measurement set 3  Solution: [4.90243902 5.6097561  5.53658537]  Residual norm: 0.0
Direct solution for first set: [5. 5. 5.]
```

## C. Changing an input
Doubling b doubles the solution exactly ([5.3171, 5.2683, 4.7561] → [10.6341, 10.5366, 9.5122]); adding a vector to b adds its own solution. This is the linearity of Ax = b, and it is why one factorization works for every b.

## D. Interpretation
Each measurement set gives a different solution but needs no new elimination. Residuals near 1e-15 are rounding noise, so the answers are accurate. The LU answer equals the direct solver's.

## E. New case – heat conduction in a metal rod
- **Assumptions:** 300 interior nodes, diffusion number r = 1, ends held at 0 °C, a hot 20-node section of 100 °C in the middle, 300 implicit time steps.
- **Method:** each step solves (I + rL) u_new = u_old. The matrix never changes, so it is factored once.
- **Output:** identical results from both methods; the peak falls from 100 °C to 31.73 °C and the hot region spreads from 20 to 132 nodes; total heat stays 2000 because it has not reached the ends. Solving from scratch each step took 0.33 s versus 0.014 s with LU (about 23× faster).
- **Interpretation:** heat spreads out and the peak flattens. Reusing the factorization is the main time saver in simulations that repeat the same matrix.
