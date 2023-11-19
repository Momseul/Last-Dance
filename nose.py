from math import isclose
import math
import numpy as np
import sympy as sp




def bisection_function(function_text, a, b, tol, max_count):
    results = {
        "iterations": [],
        "conclusion": None
    }

    if max_count < 0:
        raise ValueError("Max iterations must be non-negative: iteration = {}".format(max_count))

    if math.isnan(eval(function_text, {"x": a})):
        raise ValueError("a is not defined in the domain of the function: a = {}".format(a))

    if math.isnan(eval(function_text, {"x": b})):
        raise ValueError("b is not defined in the domain of the function: b = {}".format(b))

    if a >= b:
        raise ValueError("a must be less than b: a = {}, b = {}".format(a, b))

    if tol < 0:
        raise ValueError("Tolerance must be non-negative: tol = {}".format(tol))

    count = 1
    mid = (a + b) / 2
    error = mid

    while error > tol and count < max_count:
        fa = eval(function_text, {"x": a})
        fb = eval(function_text, {"x": b})
        fm = eval(function_text, {"x": mid})

        if fa * fm < 0:
            b = mid
            fb = fm
        else:
            a = mid
            fa = fm

        mid = (a + b) / 2
        fm = eval(function_text, {"x": mid})
        error = (b - a) / 2

        results["iterations"].append([
            count,
            format(a, ".10f"),
            format(mid, ".10f"),
            format(b, ".10f"),
            format(fm, ".2e"),
            format(error, ".2e")
        ])

        count += 1

    results["iterations"].append([
        count,
        format(a, ".10f"),
        format(mid, ".10f"),
        format(b, ".10f"),
        format(fm, ".2e"),
        format(error, ".2e")
    ])

    if fm == 0:
        results["conclusion"] = "The root was found at m = {}".format(format(mid, ".15f"))
        return results
    elif error <= tol:
        results["conclusion"] = "An approximation of the root was found at m = {}".format(format(mid, ".15f"))
        return results
    elif count < max_count and error > tol:
        raise ValueError("No root was found within the interval of the function")

    elif count == max_count:
        results["conclusion"] = "The method failed to find a satisfactory root within the specified iterations and tolerance"
        return results
    else:
        results["conclusion"] = "The method exploded"
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

result = bisection_function(example_function, a, b, tolerance, max_iterations)
print(result)
