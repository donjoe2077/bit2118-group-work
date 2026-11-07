"""Task 05 extension - matrix algebra.

PART 1: change the rotation angle (45 -> 90 degrees) in the graphics example.
PART 2: new case - forward kinematics of a two-link robot arm using rotation matrices.
Link lengths and angles are ASSUMED.
"""
import numpy as np


def rot(deg):
    t = np.deg2rad(deg)
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])


# ---------------- PART 1: parameter change ----------------
points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
scale = np.diag([2.0, 1.5])
print("PART 1 - rotate by 90 degrees then scale (2, 1.5)")
T = rot(90) @ scale
print("Transformed points:\n", np.round(points @ T.T, 4))
print("Determinant:", round(np.linalg.det(T), 4), "(area scale factor = 2 x 1.5 = 3, rotation does not change area)")
print()

# ---------------- PART 2: new case ----------------
L1, L2 = 0.5, 0.3     # link lengths in metres


def end_effector(theta1, theta2):
    """Rotate each link by the accumulated joint angle and add the vectors."""
    elbow = rot(theta1) @ np.array([L1, 0.0])
    tip = elbow + rot(theta1 + theta2) @ np.array([L2, 0.0])
    return elbow, tip


print("PART 2 - two-link arm (L1=0.5 m, L2=0.3 m)")
for t1, t2 in [(0, 0), (30, 45), (90, -90), (45, 180)]:
    elbow, tip = end_effector(t1, t2)
    reach = np.linalg.norm(tip)
    print(f"theta1={t1:>3}, theta2={t2:>4}: elbow=({elbow[0]:.3f},{elbow[1]:.3f}) "
          f"tip=({tip[0]:.3f},{tip[1]:.3f}) distance from base={reach:.3f} m")
print(f"Maximum reach = {L1+L2:.2f} m, minimum reach = {abs(L1-L2):.2f} m")

# Sweep elbow angle to see the reachable distances, using one vectorised call chain
angles = np.deg2rad(np.linspace(0, 180, 7))
dist = np.sqrt(L1**2 + L2**2 + 2*L1*L2*np.cos(angles))
print("Distance from base for elbow angles 0..180 deg:", np.round(dist, 3))
