# Task 08 – Iterative Methods for Linear Systems

**Concept:** improve a guess repeatedly (Jacobi, Gauss-Seidel) until the change is below a tolerance.
**Code:** `code/Task_08_iterative_linear.py` · **Figure:** `figures/task_08.png` · **Extension:** `extensions/Task_08_ext_grid_size.py`

## B. Inputs and mathematical operations
- **Inputs:** a 5×5 tridiagonal matrix (2 on the diagonal, −1 beside it) and b = [100, 0, 0, 0, 20] (boundaries at 100 °C and 20 °C); tolerance 1e-8.
- **Operations:** Jacobi uses only old values; Gauss-Seidel uses updated values immediately. The error is the largest change between iterations.

## Output of the original program
```
Jacobi temperatures:       [86.667 73.333 60.000 46.667 33.333]
Gauss-Seidel temperatures: [86.667 73.333 60.000 46.667 33.333]
Direct solution:           [86.667 73.333 60.000 46.667 33.333]
Jacobi iterations: 150      Gauss-Seidel iterations: 75
```

## C. Changing an input
- Tolerance 1e-4 / 1e-8 / 1e-12: Gauss-Seidel needs 43 / 75 / 107 iterations (Jacobi 86 / 150 / 214). Each extra digit of accuracy costs a roughly constant number of iterations.
- Left boundary 80 °C instead of 100 °C: temperatures become 70, 60, 50, 40, 30 – the whole profile shifts.

## D. Interpretation of the graph
The y-axis is logarithmic, so the nearly straight falling lines mean the error shrinks by a constant factor each iteration. The Gauss-Seidel line is steeper: it needs about half the iterations. Both methods end at the direct answer, a smooth straight-line temperature drop from the hot end to the cold end.

## E. New case – longer rods
- **Assumptions:** same boundaries (100 °C and 20 °C), n = 5, 10, 20, 40 interior points, tolerance 1e-8.
- **Output:**

| n | Jacobi iterations | Gauss-Seidel iterations |
|---|---|---|
| 5 | 150 | 75 |
| 10 | 486 | 245 |
| 20 | 1672 | 842 |
| 40 | 5935 | 2993 |

- **Interpretation:** doubling the grid roughly triples or quadruples the iterations, so fine grids make plain iterative methods slow. This is why large simulations use faster variants and why the method choice depends on problem size.
