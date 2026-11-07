# Task 04 – Floating-Point Arithmetic and Numerical Errors

**Concept:** computers store most decimals approximately, so tiny errors appear and can grow.
**Code:** `code/Task_04_numerical_errors.py` · **Extension:** `extensions/Task_04_ext_accumulated_error.py`

## B. Inputs and mathematical operations
- **Inputs:** 0.1 + 0.2 compared with 0.3; √2 versus the approximation 1.414; and x = 1e-4, 1e-8, 1e-12 in the expression (√(1+x) − 1)/x.
- **Operations:** exact equality, `np.isclose`, absolute error |true − approx|, relative error absolute/|true|, and an algebraically equivalent stable form 1/(√(1+x)+1).

## Output of the original program
```
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

## C. Changing an input
- Tolerance: with `atol=1e-17, rtol=0` the comparison is **False** (the real difference is 5.55e-17); with `atol=1e-9` it is **True**. The answer depends on the tolerance you choose.
- x pushed to 1e-14 gives a direct value of 0.4885 and at 1e-16 it gives **0.0**, while the stable form stays at 0.5.

## D. Interpretation
0.1 has no exact binary form, so 0.1 + 0.2 is stored as 0.30000000000000004 and `==` fails. Use a tolerance. The √2 example shows 1.414 is wrong by only 0.015 %. In the last loop the true answer is 0.5; the direct formula subtracts two almost equal numbers (catastrophic cancellation) and loses digits, while the rearranged formula is accurate. Choosing a stable formula matters more than a smaller step.

## E. New case – adding 0.1 one million times
- **Assumptions:** a system keeps a running total by repeatedly adding 0.1; the true total is 100,000.
- **Output:**

| Method | Result | Absolute error |
|---|---|---|
| float64 running loop | 100000.0000013 | 1.3e-06 |
| float32 running loop | 100958.34 | 958 (0.96 %) |
| `np.sum` (pairwise) | 100000.0 | 2.9e-11 |
| `math.fsum` | 100000.0 | 0 |

- **Interpretation:** small errors add up. Single precision (float32) is off by nearly 1 000 after a million additions; double precision is far better, and algorithms designed to reduce accumulation (`np.sum`, `math.fsum`) are best. Use higher precision or better summation when totals matter (banking, GPS).
