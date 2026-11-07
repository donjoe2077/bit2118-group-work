# Task 13 – Interpolation

**Concept:** estimate values between known points with lines (linear) or smooth cubic pieces (spline).
**Code:** `code/Task_13_interpolation.py` · **Figure:** `figures/task_13.png` · **Extension:** `extensions/Task_13_ext_river_gauge.py`

## B. Inputs and mathematical operations
- **Inputs:** hourly temperatures at 08:00–14:00 (18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0 °C); target times every 10 minutes and 10:30.
- **Operations:** `interp1d` (linear) and `CubicSpline` evaluated at the new times.

## Output of the original program
```
Linear estimate at 10:30: 23.25 C
Cubic estimate at 10:30: 23.36 C
```

## C. Changing an input
Other times: at 09:30 linear 21.25 °C and cubic 21.32 °C; at 13:45 linear 25.125 and cubic 25.25. Outside the data (14:30) linear interpolation refuses (ValueError) while the cubic spline extrapolates to 24.20 °C, a guess that bends back down and cannot be trusted.

## D. Interpretation of the graph
Dots are the real hourly readings. The linear estimate is a set of straight segments with corners at each hour; the cubic spline is a smooth curve through the same dots that rounds off the warming slowdown near noon. Between 10:00 and 11:00 the spline sits above the line because the temperature is rising but slowing. Interpolation is safe inside the data range and risky outside it.

## E. New case – river gauge with missing readings
- **Assumptions:** water level every 3 hours (1.20, 1.18, 1.25, 1.60, 2.10, 2.35, 2.05, 1.55, 1.30 m, illustrative). Each interior reading is hidden in turn and predicted from the rest.
- **Output:** mean absolute error 0.126 m for linear versus 0.030 m for cubic. If the 15:00 reading (2.35 m, the flood peak) is lost, the spline estimates 2.28 m.
- **Interpretation:** the spline wins on smoothly changing data, but even it underestimates the peak, because a peak is the hardest value to recover from its neighbours. For flood monitoring a missing peak reading should be flagged, not trusted blindly.
