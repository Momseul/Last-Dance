from flask import Flask, render_template, request
import math
import numpy as np
from math import isclose, log
from sympy import symbols, sympify, lambdify, parse_expr
import sympy as sp

app = Flask(__name__)

def bisection_method(equation_lambda, a, b, tol, max_iterations):
    try:
        
        f_a = equation_lambda(a)
        f_b = equation_lambda(b)
        print("estoy aqui")
        # Check for complex values
        if any(isinstance(val, complex) for val in [f_a, f_b]):
            raise ValueError("Initial points 'a' and 'b' must be within the function's domain.")

        if a >= b:
            raise ValueError("'a' must be less than 'b': a = {}, b = {}".format(a, b))

        if tol < 0:
            raise ValueError("Tolerance must be non-negative: tol = {}".format(tol))

        iteration_count = 1
        results = {"iterations": []}

        while iteration_count <= max_iterations:
            m = (b + a ) / 2
            f_m = equation_lambda(m)

            
            if any(isinstance(val, complex) for val in [f_m]):
                raise ValueError("Function value at midpoint is not within the domain: midpoint = {}".format(m))

            results["iterations"].append([
                iteration_count,
                a,
                m,
                b,
                f_m,
                (b - a) / 2
            ])

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

    except Exception as e:
        return {"error": str(e)}


def parse_function_alt(equation_str):
    x = sp.symbols('x')
    equation = sp.sympify(equation_str)
    return sp.lambdify(x, equation, modules=['numpy'])



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <a href='/biseccion'>Go to Bisección</a>"



@app.route("/biseccion", methods=['GET', 'POST'])
def biseccion():
    parsed_equation = None  # Default value
    error_details = None

    if request.method == 'POST':
        equation_str = request.form['equation']
        a = float(request.form['a'])
        b = float(request.form['b'])
        tol = float(request.form['tol'])
        max_iterations = int(request.form['max_iterations'])

        x = symbols('x')
        try:
            # Parse the user-provided equation
            parsed_equation = parse_function_alt(equation_str)
            
            results = bisection_method(parsed_equation, a, b, tol, max_iterations)
            
        except ValueError as ve:
            return render_template('biseccion.html', error=str(ve), equation=parsed_equation)
        except Exception as e:
            error_details = str(e)
            return render_template('biseccion.html', error="An unexpected error occurred.", equation=parsed_equation, error_details=error_details)

        return render_template('biseccion.html', equation=parsed_equation, results=results)

    return render_template('biseccion.html', equation=parsed_equation)

if __name__ == "__main__":
    app.run(debug=True)