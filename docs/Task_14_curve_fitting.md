# Task 14 – Curve Fitting and Approximation

**Concept:** choose model parameters that minimise the sum of squared residuals.
**Code:** `code/Task_14_curve_fitting.py` · **Figure:** `figures/task_14.png` · **Extension:** `extensions/Task_14_ext_growth_curve.py`

## B. Inputs and mathematical operations
- **Inputs:** users = 50…350 and response times 82, 95, 115, 145, 185, 238, 305 ms; quadratic model y = ax² + bx + c.
- **Operations:** `curve_fit` (least squares), RMSE = √mean((y − ŷ)²), prediction at 400 users.

## Output of the original program
```
Fitted model: y = 0.002167x^2 + -0.1345x + 85.00
RMSE: 1.55 ms
Predicted response at 400 users: 377.86 ms
```

## C. Changing an input
Polynomial degree changed:

| Degree | RMSE | Prediction at 400 users |
|---|---|---|
| 1 (line) | 18.83 ms | 312.9 ms |
| 2 | 1.55 ms | 377.9 ms |
| 3 | 0.14 ms | 387.9 ms |

A straight line cannot follow the accelerating curve (large error). The cubic fits seven points almost perfectly but may be fitting noise; its prediction beyond the data differs by 10 ms from the quadratic.

## D. Interpretation of the graph
Dots are the measurements; the curve passes within about 1.5 ms of each. Response time grows slowly at low load and then faster, so adding users costs more each time. The extension to 400 users is a prediction beyond the data and should be treated with caution.

## E. New case – plant growth (logistic curve)
- **Assumptions:** **synthetic** data: logistic growth (maximum 120 cm) sampled every 5 days for 40 days with random noise (seed 7).
- **Output:** logistic fit gives maximum height 121.1 cm, rate 0.179/day, midpoint day 20.4, RMSE 1.09 cm. An exponential model has RMSE 15.12 cm; at day 60 it predicts 362 cm while the logistic predicts 121 cm.
- **Interpretation:** the right model matters more than the fitting method. Growth levels off, so the logistic curve is realistic, while the exponential keeps climbing and gives absurd forecasts.
