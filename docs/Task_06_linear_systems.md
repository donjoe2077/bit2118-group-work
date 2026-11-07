# Task 06 – Solution of Systems of Linear Equations

**Concept:** solve Ax = b for the unknown vector x.
**Code:** `code/Task_06_linear_systems.py` · **Extension:** `extensions/Task_06_ext_circuit.py`

## B. Inputs and mathematical operations
- **Inputs:** A = [[4, 2], [8, 12]] (CPU and memory use per server type) and b = [20, 72] (observed totals).
- **Operation:** `np.linalg.solve(A, b)`, then a check with A @ x and the residual b − A x.

## Output of the original program
```
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

## C. Changing an input
Totals changed to b = [22, 80]: the solution becomes 3.25 Type A and 4.5 Type B servers. These are not whole numbers, so those totals could not come from whole servers; something is wrong with the data. A dependent system (second row = 2 × first row) has determinant 0 and `solve` raises "Singular matrix" because there is no single answer.

## D. Interpretation
3 servers of type A and 4 of type B exactly reproduce 20 CPU units and 72 GB of memory. A residual of zero confirms the solution satisfies both equations.

## E. New case – mesh currents in a three-loop circuit
- **Assumptions:** R1 = 10, R2 = 20, R3 = 30, R4 = 15, R5 = 25 Ω; sources V1 = 12 V and V2 = 6 V.
- **Method:** Kirchhoff's voltage law gives a 3×3 system for the loop currents.
- **Output:** I1 = 547.7 mA, I2 = 112.8 mA, I3 = −57.8 mA; residual about 1e-16; condition number 5.08.
- **Interpretation:** the negative sign for I3 means that loop's current flows opposite to the direction assumed. The shared resistors carry the difference of neighbouring loop currents (434.9 mA through R4, 170.6 mA through R5). A small condition number means the answer is not sensitive to rounding.
