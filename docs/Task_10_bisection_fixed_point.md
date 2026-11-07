# Task 10 – Root Finding: Bisection and Fixed-Point Methods

**Concept:** find r with f(r) = 0 by halving a bracket (bisection) or repeating x = g(x) (fixed point).
**Code:** `code/Task_10_bisection_fixed_point.py` · **Figure:** `figures/task_10.png` · **Extension:** `extensions/Task_10_ext_break_even.py`

## B. Inputs and mathematical operations
- **Inputs:** f(T) = T − 25 − 10·e^(−T/20); bracket [20, 40]; tolerance 1e-10; fixed-point form T = 25 + 10·e^(−T/20) starting at 30 °C.
- **Operations:** repeated halving keeping the half with a sign change; repeated evaluation of g(T).

## Output of the original program
```
Bisection equilibrium temperature: 27.525211 C   (38 halvings)
Fixed-point equilibrium temperature: 27.525211 C (13 iterations)
```

## C. Changing an input
The constant 10 was changed to 20 and 30:

| A | Equilibrium T | Bisection halvings | Fixed-point iterations |
|---|---|---|---|
| 10 | 27.5252 °C | 38 | 13 |
| 20 | 29.5615 °C | 38 | 17 |
| 30 | 31.2792 °C | 38 | 22 |

A larger heat term raises the equilibrium. Bisection always needs about log₂(20/1e-10) ≈ 38 halvings; fixed point slows as A grows because the slope of g gets closer to 1.

## D. Interpretation of the graph
The curve crosses zero once near T = 27.5 °C (dashed line). To the left the function is negative (heat gain below heat loss), to the right positive. The crossing is the equilibrium temperature where gain equals loss. Both methods find the same value, so the answer is reliable.

## E. New case – business break-even points
- **Assumptions:** price = 100 − 0.02q, cost = 2000 + 30q + 0.01q² (illustrative); profit(q) = revenue − cost.
- **Method:** bisection in two brackets, [0, 100] and [1000, 3000], because profit changes sign twice.
- **Output:** profitable between **q = 28.9** and **q = 2304.4** units; best volume about 1167 units with profit 38,833. If the base price drops to 90, the range narrows to 33.9–1966.1 units and the best profit falls to 28,000.
- **Interpretation:** the business loses money on tiny volumes (fixed costs) and on huge volumes (price falls, costs rise). A lower price shrinks the profitable window.
