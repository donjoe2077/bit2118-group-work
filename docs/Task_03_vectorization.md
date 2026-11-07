# Task 03 – Mathematical Functions and Vectorization

**Concept:** apply one operation to a whole array instead of looping element by element.
**Code:** `code/Task_03_vectorization.py` · **Extension:** `extensions/Task_03_ext_transactions.py`

## B. Inputs and mathematical operations
- **Input:** 1,000,000 simulated latencies in milliseconds, uniform between 5 and 250 (seed 42).
- **Operations:** seconds = ms / 1000, then squared = seconds². Done twice: with a Python `for` loop and with one vectorized expression, timed with `timeit`.

## Output of the original program
```
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1932 s
Vectorized time: 0.0034 s
Approximate speed-up: 56.8x
```
(Timings depend on the computer and change slightly on every run.)

## C. Changing an input
The number of values N was changed (extension, Part 1):

| N | Loop | Vectorized | Speed-up |
|---|---|---|---|
| 1,000 | 0.00013 s | 0.000007 s | 18× |
| 100,000 | 0.0126 s | 0.000845 s | 15× |
| 1,000,000 | 0.204 s | 0.0029 s | 70× |

Both methods slow down as N grows, but the vectorized one stays far cheaper because the loop runs in Python while NumPy runs compiled code.

## D. Interpretation
The two methods give the same numbers; only the cost differs. At a million values the vectorized version is roughly 50–70 times faster, which matters when a calculation is repeated millions of times in simulations or signal processing.

## E. New case – fees and currency for mobile-money style transactions
- **Assumptions (all simulated):** 1,000,000 amounts drawn from a log-normal distribution; fee = 1 % of the amount, at least 5 KES and at most 100 KES; exchange rate 129 KES/USD.
- **Method:** `np.clip(0.01*amount, 5, 100)` applies the min/max rule to every transaction at once.
- **Output:** results identical to the loop version; total fees 11,674,873 KES; average fee 11.67 KES (1.06 % of money moved); 3,332 transactions hit the cap; loop 0.33 s vs vectorized 0.0054 s (about 61× faster).
- **Interpretation:** because of the 5 KES floor, small payments pay more than 1 %, so the overall fee rate is slightly above 1 %. Vectorized rules like `clip` replace `if/elif` branches inside loops.
