# Task 05 – Matrix Algebra and Matrix Operations

**Concept:** matrices describe transformations; matrix multiplication combines them.
**Code:** `code/Task_05_matrix_algebra.py` · **Extension:** `extensions/Task_05_ext_robot_arm.py`

## B. Inputs and mathematical operations
- **Inputs:** four corners of a unit square, a 45° rotation matrix, and a scaling matrix diag(2, 1.5).
- **Operations:** combined matrix T = Rotation @ Scale, transformed points = points @ Tᵀ, determinant of T.

## Output of the original program
```
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

## C. Changing an input
Angle changed from 45° to 90°. The square now maps to corners (0,0), (0,2), (−1.5,2), (−1.5,0): a clean quarter turn with the 2× and 1.5× stretches now lying along the y and x axes. The determinant stays 3, because a rotation does not change area and the scales multiply to 2 × 1.5 = 3.

## D. Interpretation
Scaling first and then rotating turns the unit square into a rotated rectangle. The determinant 3 says its area is three times the original. A determinant of 0 would mean the transformation collapses the shape and cannot be undone.

## E. New case – two-link robot arm
- **Assumptions:** link lengths 0.5 m and 0.3 m; joint angles chosen for illustration.
- **Method:** rotate each link by its accumulated joint angle and add the vectors.
- **Output:** straight arm (0°, 0°) reaches 0.800 m; (30°, 45°) puts the tip at (0.511, 0.540) m (0.743 m from the base); folding the elbow 180° brings the tip back to 0.200 m from the base.
- **Interpretation:** the reachable distance runs from |L1 − L2| = 0.2 m to L1 + L2 = 0.8 m. Matrix multiplication chains joint rotations, which is how graphics engines and robots compute positions.
