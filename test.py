from math import isclose
import math
import numpy as np
import sympy as sp

def bisection_method(function, a, b, tol, max_iterations):
    results = {
        "iterations": [],
        "conclusion": None
    }

    if max_iterations < 0:
        raise ValueError("Max iterations must be non-negative: {}".format(max_iterations))

    f_a = function(a)
    f_b = function(b)


    if f_a.imag or f_b.imag:
        raise ValueError("Initial points 'a' and 'b' must be within the function's domain.")

    if a >= b:
        raise ValueError("'a' must be less than 'b': a = {}, b = {}".format(a, b))

    if tol < 0:
        raise ValueError("Tolerance must be non-negative: tol = {}".format(tol))

    iteration_count = 1

    while iteration_count <= max_iterations:
        m = (a + b) / 2
        f_m = function(m)

        results["iterations"].append([
            iteration_count,
            a,
            m,
            b,
            f_m,
            (b - a) / 2
        ])

        if f_m.imag:
            raise ValueError("Function value at midpoint is not within the domain: midpoint = {}".format(m))

        if isclose(f_m, 0, abs_tol=tol):
            results["conclusion"] = "Root found at m = {}".format(m)
            return results
        elif f_a * f_m < 0:
            b = m
            f_b = f_m
        else:
            a = m
            f_a = f_m

        iteration_count += 1

    results["conclusion"] = "No root found in the interval of the function"
    return results

def parse_function(equation_str):
    x = sp.symbols('x')
    equation = sp.sympify(equation_str)
    return sp.lambdify(x, equation, modules=['numpy'])

# Ejemplo de uso:
""" def example_function(x):
    return np.log(np.sin(x)**2 + 1) - (1/2) """

equation_str = "log(sin(x)^2 + 1)-(1/2)"
example_function = parse_function(equation_str)

a = 0
b = 1
tolerance = 1e-7
max_iterations = 100

result = bisection_method(example_function, a, b, tolerance, max_iterations)
print(result)
