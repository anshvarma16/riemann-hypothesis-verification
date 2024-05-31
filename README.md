# Riemann Hypothesis Verification

This repository contains Python code to verify the Riemann Hypothesis using symbolic manipulation with SymPy and numerical computation with mpmath. The Riemann Hypothesis is a famous conjecture in number theory, positing that all non-trivial zeros of the Riemann zeta function lie on the critical line with real part 1/2.

## Features

- Symbolic manipulation of the completed zeta function and its logarithmic derivative using SymPy.
- Numerical evaluation of functions using mpmath, a pure Python library for arbitrary precision numerics.
- Implementation of the argument principle to count zeros of the zeta function in specified regions.
- Computation of points along the critical line and counting of sign changes to locate zeros.
- Verification of the Riemann Hypothesis up to a specified limit.
- Plotting of zeros along the critical line for visualization.

## Getting Started

1. Download the code to your local machine

2. Ensure you have Python 3.x installed along with required libraries (SymPy, mpmath, NumPy, and Matplotlib).

```bash
pip install sympy mpmath numpy matplotlib
```

3. Adjust the parameters in the code, such as the limit for verification.

4. Run the script to verify the Riemann Hypothesis and visualize the distribution of zeros along the critical line.

```bash
python verify_riemann_hypothesis.py
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This code was inspired by discussions on the Riemann Hypothesis and computational methods for its verification. Special thanks to SymPy and mpmath developers for their excellent libraries.
