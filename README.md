# BIT 2118 Scientific Computing – Group Work

Author: Abdirizack Ibrahim (Bsccs202541789)

This repository holds my individual submission for the Scientific Computing group work (Tasks 2–20). For every task it contains:

- the program from the brief, run and saved with its real output,
- a write-up covering the inputs and operations, a parameter change, the meaning of the output and graph, and
- a modified program that solves a different but related real-world case, with its assumptions, input data, output and interpretation.

An interactive dashboard (`dashboard/index.html`) shows every task with sliders so each input can be changed and the result watched.

## Repository layout

| Folder | Contents |
|---|---|
| `code/` | `Task_02_…` to `Task_20_…` programs from the brief. Plots are saved to `figures/` instead of opening a window. |
| `extensions/` | One program per task: Part 1 changes an input of the original, Part 2 solves a new real-world case. |
| `docs/` | One Markdown write-up per task (points B to E of the instructions). |
| `outputs/` | Saved console output of every program in `code/` and `extensions/`. |
| `figures/` | Graphs produced by the programs. |
| `dashboard/` | The interactive workbook (open `index.html` in a browser). |

## Tasks

| Task | Topic | Code | New case |
|---|---|---|---|
| 2 | NumPy arrays | `Task_02_numpy_arrays.py` | Greenhouse soil moisture |
| 3 | Vectorization | `Task_03_vectorization.py` | Transaction fees and currency conversion |
| 4 | Floating-point errors | `Task_04_numerical_errors.py` | Adding 0.1 a million times |
| 5 | Matrix algebra | `Task_05_matrix_algebra.py` | Two-link robot arm |
| 6 | Linear systems | `Task_06_linear_systems.py` | Three-loop circuit |
| 7 | LU decomposition | `Task_07_gaussian_lu.py` | Heat conduction in a rod |
| 8 | Iterative methods | `Task_08_iterative_linear.py` | Longer rods |
| 9 | Eigenvalues | `Task_09_eigenvalues.py` | PageRank of five web pages |
| 10 | Bisection and fixed point | `Task_10_bisection_fixed_point.py` | Business break-even points |
| 11 | Newton and secant | `Task_11_newton_secant.py` | True interest rate of a loan |
| 12 | Nonlinear equations | `Task_12_nonlinear_equations.py` | Phone position from two towers |
| 13 | Interpolation | `Task_13_interpolation.py` | River gauge with a lost reading |
| 14 | Curve fitting | `Task_14_curve_fitting.py` | Plant growth (logistic curve) |
| 15 | Numerical differentiation | `Task_15_numerical_differentiation.py` | Car acceleration from speed |
| 16 | Numerical integration | `Task_16_numerical_integration.py` | Total rainfall from a storm |
| 17 | Euler method | `Task_17_euler_ode.py` | SIR epidemic model |
| 18 | ODEs with SciPy | `Task_18_scipy_ode.py` | Vehicle suspension |
| 19 | Optimization | `Task_19_optimization.py` | Cheapest fence for a farm |
| 20 | Monte Carlo | `Task_20_monte_carlo.py` | Bus journey time |

Each write-up is in `docs/` under the same name as its program, with a `.md` ending.

## Running the programs

Requires Python 3.10 or newer with NumPy 2.x (the brief uses `np.trapezoid`), SciPy and Matplotlib.

```bash
pip install numpy scipy matplotlib
python code/Task_10_bisection_fixed_point.py
python extensions/Task_10_ext_break_even.py
```

Run any file from the repository root. Programs that draw graphs save them in `figures/`.

## Data and assumptions

The data in the original programs come from the brief. The new cases use **assumed or synthetic values chosen for illustration** (for example the river levels, the plant heights, the circuit resistors and the epidemic rates); they are not measurements of real systems. Each write-up states its assumptions. Timing results (Tasks 3 and 7) depend on the computer and change from run to run.
"# BIT2118" 
