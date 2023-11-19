from sympy import symbols, lambdify

def newton_r_method(f, derivative, x0, tol, max_count):
    error = 0
    count = 0
    x = symbols('x')
    
    fX0 = f(x0)
    results = {
        "iterations": [],
        "conclusion": None
    }
    
    if max_count < 0:
        raise ValueError("Max iterations is < 0: iterations = {}".format(max_count))
    if tol < 0:
        raise ValueError("tol is an incorrect value: tol = {}".format(tol))
    if f(x0).imag:
        raise ValueError("x0 isn't defined in the domain of the function f: x0 = {}".format(x0))
    
    results["iterations"].append([
        count,
        x0,
        fX0,
        None
    ])
    
    if fX0 == 0:
        results["conclusion"] = "x{} is the root: {}".format(count, x0)
        return results
    
    derivativeX0 = derivative(x0)
    
    if derivativeX0 == 0:
        raise ValueError("The point evaluated in the derivative must be different from 0")
    
    xN = x0 - fX0 / derivativeX0
    fXN = f(xN)
    
    count += 1
    error = abs(x0 - xN)
    
    results["iterations"].append([
        count,
        xN,
        fXN,
        error
    ])
    
    while error > tol and count < max_count and fXN != 0:
        x0 = xN
        fX0 = fXN
        derivativeX0 = derivative(x0)
        xN = xN = x0 - fX0 / derivativeX0
        error = abs(x0 - xN)
        fXN = f(xN)
        count += 1
        
        if derivativeX0.imag:
            raise ValueError("xi isn't defined in the domain of the derivative f: xi = {}".format(x0))
        if fXN.imag:
            raise ValueError("xi isn't defined in the domain of the function f: xi = {}".format(xN))
        
        results["iterations"].append([
            count,
            xN,
            fXN,
            error
        ])
    
    if fXN == 0:
        results["conclusion"] = "The root was found for x{} = {}".format(count, xN)
        return results
    elif error <= tol:
        results["conclusion"] = "An approximation of the root was found for x{} = {}".format(count, xN)
        return results
    elif count == max_count:
        results["conclusion"] = "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"
        return results
    else:
        results["conclusion"] = "The method exploded"
        return results
