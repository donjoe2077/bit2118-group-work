# Task 11 – Root Finding: Newton-Raphson and Secant Methods

**Concept:** Newton uses xₙ₊₁ = xₙ − f/f′; secant replaces f′ with a slope from two points.
**Code:** `code/Task_11_newton_secant.py` · **Extension:** `extensions/Task_11_ext_loan_rate.py`

## B. Inputs and mathematical operations
- **Inputs:** cash flows −10000, 3000, 3500, 4000, 2500 (an investment and four yearly returns); starting guesses 0.10 (Newton) and 0.05, 0.20 (secant).
- **Operation:** find the rate r where NPV(r) = Σ cashflow/(1+r)ᵗ equals zero (the internal rate of return).

## Output of the original program
```
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
Newton iterations: 4, Secant iterations: 7
NPV at Newton solution: 0.000000
```

## C. Changing an input
- Initial investment 10,000 / 11,000 / 9,000 gives IRR 11.54 % / 7.14 % / 16.73 %: paying more for the same returns lowers the return rate.
- Starting guess 0.10 and 0.50 both reach 11.54 % (4 and 8 steps), but a start of 1.00 converged to −154 %, another mathematical root that is meaningless as an interest rate. Newton needs a sensible start.

## D. Interpretation
The project returns about 11.5 % per year; at that rate the discounted inflows exactly equal the cost. Newton needed 4 steps and secant 7: Newton is faster but needs the derivative, secant needs only function values.

## E. New case – true interest rate of a loan
- **Assumptions:** a loan of 100,000 received now, repaid by 12 monthly instalments of 9,000 (illustrative).
- **Output:** monthly rate 1.204346 % (Newton 4 steps, secant 6 steps); effective annual rate 15.45 %; simple "monthly × 12" rate 14.45 %. Total repaid 108,000, i.e. 8 % more than borrowed.
- **Interpretation:** the headline "8 % extra" understates the cost because the borrower repays gradually, so the average money borrowed is much less than 100,000. The proper rate is about 15 % a year, which is why root finding is used for loan and investment comparisons.
