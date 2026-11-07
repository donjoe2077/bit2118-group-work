# Task 15 – Numerical Differentiation

**Concept:** approximate a rate of change from nearby values using finite differences.
**Code:** `code/Task_15_numerical_differentiation.py` · **Figure:** `figures/task_15.png` · **Extension:** `extensions/Task_15_ext_acceleration.py`

## B. Inputs and mathematical operations
- **Inputs:** GPS time 0–6 s and position 0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0 m.
- **Operations:** forward difference at the first point, central difference (x[i+1] − x[i−1])/(t[i+1] − t[i−1]) inside, backward difference at the last point.

## Output of the original program
```
t=0s  speed=4.80 m/s   t=1s  5.10   t=2s  5.65   t=3s  6.25
t=4s  speed=6.95 m/s   t=5s  7.65   t=6s  8.00
```

## C. Changing an input
The step size h was varied on sin(x) at x = 1 (extension, Part 1). With h = 0.1 / 0.01 / 0.001 the forward error is 4.3e-2 / 4.2e-3 / 4.2e-4 (shrinks ∝ h) and the central error is 9.0e-4 / 9.0e-6 / 9.0e-8 (shrinks ∝ h²). At h = 1e-12 round-off dominates and both errors grow again (4.3e-5 and 1.2e-5).

## D. Interpretation of the graph
The speed line rises from 4.8 to 8.0 m/s: the vehicle is accelerating steadily. The end points use one-sided differences and are less accurate than interior points. Real GPS data are noisy, and differentiation amplifies noise, so smoothing may be needed first.

## E. New case – car acceleration from speed readings
- **Assumptions:** speeds 0, 18, 35, 50, 60, 65 km/h every 2 s (illustrative), converted to m/s.
- **Output:** acceleration 2.57, 2.43, 2.22, 1.74, 1.04, 0.35 m/s²; peak 2.57 m/s² at the start; distance covered by trapezoid ≈ 108.6 m.
- **Interpretation:** the car accelerates hardest at the start, then the acceleration falls toward zero as speed levels off. The same method turns position into speed and speed into acceleration.
