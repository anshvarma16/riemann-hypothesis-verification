from sympy import *
import mpmath
import numpy as np
import matplotlib.pyplot as plt

s = symbols('s')

# Define the completed zeta function
Z = pi**(-s/2)*gamma(s/2)*zeta(s)

# Define the logarithmic derivative of Z
D = simplify(Z.diff(s)/Z)

# Convert symbolic expressions to numerical functions
Z_func = lambdify(s, Z, 'mpmath')
D_func = lambdify(s, D, modules=['mpmath',
                                 {'Derivative': lambda expr, z: mpmath.zeta(z, derivative=1)}])

# Function to count zeros using argument principle
def argument_count(func, N, maxdegree=6):
    return 1/(2*mpmath.pi*1j)*(mpmath.quad(func,
                                            [1 + 0.1j, 1 + N*1j, 0 + N*1j, 0 + 0.1j,  1 + 0.1j],
                                            maxdegree=maxdegree))

# Function to compute points of Z along the critical line
def compute_points(Z_func, N, npoints=10000, dps=15):
    import warnings
    old_dps = mpmath.mp.dps
    points = np.linspace(0, N, npoints)
    try:
        mpmath.mp.dps = dps
        L = [mpmath.chop(Z_func(i)) for i in 1/2 + points*1j]
    finally:
        mpmath.mp.dps = old_dps
    if L[-1] == 0:
        # mpmath will give 0 if the precision is not high enough, since Z
        # decays rapidly on the critical line.
        warnings.warn("You may need to increase the precision")
    return L

# Function to count sign changes in a list of real values
def sign_changes(L):
    changes = 0
    assert im(L[0]) == 0, L[0]
    s = sign(L[0])
    for i in L[1:]:
        assert im(i) == 0, i
        s_ = sign(i)
        if s_ == 0:
            # Assume these got chopped to 0
            continue
        if s_ != s:
            changes += 1
        s = s_
    return changes

# Function to plot points along the critical line
def plot_points(L, N):
    npoints = len(L)
    points = np.linspace(0, N, npoints)
    p = [mpmath.log(abs(i)) for i in L]
    plt.figure()
    plt.plot(points, p)
    plt.plot(points, [0]*npoints, linestyle=':')

# Verify Riemann Hypothesis up to a certain limit
def verify_riemann_hypothesis(limit):
    zeros_count = argument_count(D_func, limit)
    print(f"Number of zeros up to {limit}: {zeros_count.real}")

    L = compute_points(Z_func, limit)
    sign_changes_count = sign_changes(L)
    print(f"Number of sign changes up to {limit}: {sign_changes_count}")

    if zeros_count.real == sign_changes_count:
        print("Riemann Hypothesis verified up to", limit)
    else:
        print("Riemann Hypothesis not verified up to", limit)

    plot_points(L, limit)
    plt.show()

# Example usage:
verify_riemann_hypothesis(100)
