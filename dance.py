from flask import Flask, render_template, request
import math
import numpy as np
from math import isclose, log
from sympy import symbols, sympify, lambdify, parse_expr
import sympy as sp
from biseccion import biseccion_method
from false import regula_falsi
from fpoint import fixed_point_method
from newtonr import newton_r_method
from secant import secant_method
from mroots import multiple_roots_method

app = Flask(__name__)



def parse_function_alt(equation_str):
    x = sp.symbols('x')
    equation = sp.sympify(equation_str)
    return sp.lambdify(x, equation, modules=['numpy'])

@app.route("/")
def hello_world():
    links = "<p>Hello, World!</p>"
    links += "<ul>"
    links += "<li><a href='/biseccion'>Bisección</a></li>"
    links += "<li><a href='/false-position'>False position</a></li>"
    links += "<li><a href='/fixed-point'>Fixed point</a></li>"
    links += "<li><a href='/newtonr'>Newton R</a></li>"
    links += "<li><a href='/secant'>Secant</a></li>"
    links += "<li><a href='/multiple-roots'>Multiple Roots</a></li>"
    links += "</ul>"
    return links

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
            results = biseccion_method(parsed_equation, a, b, tol, max_iterations)
            
        except ValueError as ve:
            return render_template('biseccion.html', error=str(ve), equation=parsed_equation)
        except Exception as e:
            error_details = str(e)
            return render_template('biseccion.html', error="An unexpected error occurred.", equation=parsed_equation, error_details=error_details)

        return render_template('biseccion.html', equation=parsed_equation, results=results)

    return render_template('biseccion.html', equation=parsed_equation)

@app.route("/false-position", methods=['GET', 'POST'])
def false_position():
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
            results = regula_falsi(parsed_equation, a, b, tol, max_iterations)
            
        except ValueError as ve:
            return render_template('false.html', error=str(ve), equation=parsed_equation)
        except Exception as e:
            error_details = str(e)
            return render_template('false.html', error="An unexpected error occurred.", equation=parsed_equation, error_details=error_details)

        return render_template('false.html', equation=parsed_equation, results=results)

    return render_template('false.html', equation=parsed_equation)

@app.route("/fixed-point", methods=['GET', 'POST'])
def fixed_point():
    parsed_equation = None  # Default value
    error_details = None

    if request.method == 'POST':
        equation_str_f = request.form['f equation']
        equation_str_g = request.form['g equation']
        x0 = float(request.form['x0'])
        tol = float(request.form['tol'])
        max_iterations = int(request.form['max_iterations'])

        x = symbols('x')
        try:
            # Parse the user-provided equation
            parsed_equation_f = parse_function_alt(equation_str_f)
            parsed_equation_g = parse_function_alt(equation_str_g)
            results = fixed_point_method(parsed_equation_f, parsed_equation_g, x0, tol, max_iterations)
            
        except ValueError as ve:
            return render_template('fixed.html', error=str(ve), equation=parsed_equation)
        except Exception as e:
            error_details = str(e)
            return render_template('fixed.html', error="An unexpected error occurred.", equation=parsed_equation, error_details=error_details)

        return render_template('fixed.html', equation=parsed_equation, results=results)

    return render_template('fixed.html', equation=parsed_equation)

@app.route("/newtonr", methods=['GET', 'POST'])
def newtonr():
    parsed_equation = None  # Default value
    error_details = None

    if request.method == 'POST':
        equation_str = request.form['equation']
        equation_str_d = request.form['derivate']
        x0 = float(request.form['x0'])
        tol = float(request.form['tol'])
        max_iterations = int(request.form['max_iterations'])

        x = symbols('x')
        try:
            # Parse the user-provided equation
            parsed_equation = parse_function_alt(equation_str)
            parsed_equation_d = parse_function_alt(equation_str_d)
            results = newton_r_method(parsed_equation, parsed_equation_d, x0, tol, max_iterations)
            
        except ValueError as ve:
            return render_template('newtonr.html', error=str(ve), equation=parsed_equation)
        except Exception as e:
            error_details = str(e)
            return render_template('newtonr.html', error="An unexpected error occurred.", equation=parsed_equation, error_details=error_details)

        return render_template('newtonr.html', equation=parsed_equation, results=results)

    return render_template('newtonr.html', equation=parsed_equation)

@app.route("/secant", methods=['GET', 'POST'])
def secant():
    parsed_equation = None  # Default value
    error_details = None

    if request.method == 'POST':
        equation_str = request.form['equation']
        x0 = float(request.form['x0'])
        x1 = float(request.form['x1'])
        tol = float(request.form['tol'])
        max_iterations = int(request.form['max_iterations'])

        x = symbols('x')
        try:
            # Parse the user-provided equation
            parsed_equation = parse_function_alt(equation_str)
            results = secant_method(parsed_equation, x0, x1, tol, max_iterations)
            
        except ValueError as ve:
            return render_template('secant.html', error=str(ve), equation=parsed_equation)
        except Exception as e:
            error_details = str(e)
            return render_template('secant.html', error="An unexpected error occurred.", equation=parsed_equation, error_details=error_details)

        return render_template('secant.html', equation=parsed_equation, results=results)

    return render_template('secant.html', equation=parsed_equation)

@app.route("/multiple-roots", methods=['GET', 'POST'])
def multiple_roots():
    parsed_equation = None  # Default value
    error_details = None

    if request.method == 'POST':
        equation_str = request.form['equation']
        equation_str_df = request.form['derivate']
        equation_str_ds = request.form['s derivate']
        x0 = float(request.form['x0'])
        tol = float(request.form['tol'])
        max_iterations = int(request.form['max_iterations'])

        x = symbols('x')
        try:
            # Parse the user-provided equation
            parsed_equation = parse_function_alt(equation_str)
            parsed_equation_df = parse_function_alt(equation_str_df)
            parsed_equation_ds = parse_function_alt(equation_str_ds)
            results = multiple_roots_method(parsed_equation, parsed_equation_df, parsed_equation_ds, x0, tol, max_iterations)
            
        except ValueError as ve:
            return render_template('mroots.html', error=str(ve), equation=parsed_equation)
        except Exception as e:
            error_details = str(e)
            return render_template('mroots.html', error="An unexpected error occurred.", equation=parsed_equation, error_details=error_details)

        return render_template('mroots.html', equation=parsed_equation, results=results)

    return render_template('mroots.html', equation=parsed_equation)










if __name__ == "__main__":
    app.run(debug=True)