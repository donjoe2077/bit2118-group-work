"""Task 11 extension - Newton-Raphson and secant.

PART 1: change the initial investment (and a poor starting guess) in the IRR problem.
PART 2: new case - true interest rate of a loan: 100,000 received now, repaid in
        12 monthly instalments of 9,000. Figures are ASSUMED.
"""
from scipy.optimize import root_scalar


def make_npv(cash_flows):
    def npv(r):
        return sum(cf / (1 + r)**t for t, cf in enumerate(cash_flows))

    def d_npv(r):
        return sum(-t * cf / (1 + r)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)
    return npv, d_npv


# ---------------- PART 1: parameter change ----------------
print("PART 1 - IRR when the initial investment changes")
for invest in (10000, 11000, 9000):
    npv, d = make_npv([-invest, 3000, 3500, 4000, 2500])
    s = root_scalar(npv, fprime=d, x0=0.10, method="newton", xtol=1e-12)
    print(f"Investment {invest}: IRR = {s.root:.4%} after {s.iterations} Newton steps")

npv, d = make_npv([-10000, 3000, 3500, 4000, 2500])
for x0 in (0.10, 0.50, 1.00):
    try:
        s = root_scalar(npv, fprime=d, x0=x0, method="newton", xtol=1e-12)
        print(f"Start {x0:.2f}: IRR = {s.root:.4%} after {s.iterations} steps")
    except Exception as exc:
        print(f"Start {x0:.2f}: failed ({exc})")
print()

# ---------------- PART 2: new case ----------------
loan = [100000] + [-9000]*12          # money received, then 12 repayments
npv, d_npv_neg = make_npv(loan)
# make_npv's derivative formula already handles any cash-flow sign
newton = root_scalar(npv, fprime=d_npv_neg, x0=0.01, method="newton", xtol=1e-14)
secant = root_scalar(npv, x0=0.005, x1=0.05, method="secant", xtol=1e-14)

monthly = newton.root
annual = (1 + monthly)**12 - 1
print("PART 2 - loan of 100,000 repaid 12 x 9,000")
print(f"Total repaid: {9000*12:,} (extra {9000*12-100000:,} = {(9000*12-100000)/100000:.0%} of the loan)")
print(f"Monthly rate  Newton: {monthly:.6%} ({newton.iterations} steps) | Secant: {secant.root:.6%} ({secant.iterations} steps)")
print(f"Effective annual rate: {annual:.2%}")
print(f"Simple annual rate (monthly x 12): {monthly*12:.2%}")
print(f"NPV at the solution: {npv(monthly):.6f}")
