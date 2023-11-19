
def multiple_roots_method(function, first_derivative, second_derivative, x0, tol, max_count):
    
    results = {
        "iterations": [],
        "conclusion": None
    }
    
    if function(x0).imag:
        raise ValueError("x0 isn't defined in the domain of the function f: x0 = {}".format(x0))
    if max_count < 0:
        raise ValueError("Max iterations is < 0: iterations = {}".format(max_count))
    if tol < 0:
        raise ValueError("tol is an incorrect value: tol = {}".format(tol))
    
    fX = function(x0)
    fXP = first_derivative(x0)
    fXS = second_derivative(x0)
    err = tol + 1
    d = fXP**2 - fX * fXS
    
    count = 0
    
    results["iterations"].append([
        count,
        x0,
        fX,
        ""
    ])
    
    x_ev = None
    
    while err > tol and d != 0 and count < max_count:
        x_ev = x0 - (fX * fXP) / (fXP**2 - fX * fXS)
        if x_ev == float('inf'):
            raise ValueError("Infinity value in step {}".format(count))
        
        fX = function(x_ev)
        fXP = first_derivative(x_ev)
        fXS = second_derivative(x_ev)
        err = abs(x_ev - x0)
        count += 1
        
        if fX.imag:
            raise ValueError("xi isn't defined in the domain of the function: xi = {}".format(x_ev))
        if fXP.imag:
            raise ValueError("xi isn't defined in the domain of the first derivative: xi = {}".format(x_ev))
        if fXS.imag:
            raise ValueError("xi isn't defined in the domain of the second derivative: xi = {}".format(x_ev))
        
        x0 = x_ev
        results["iterations"].append([
            count,
            x_ev,
            fX,
            err
        ])
    
    if fX == 0:
        results["conclusion"] = "The root was found for x = {}".format(x_ev)
    elif not (err <= tol):
        results["conclusion"] = "An approximation of the root was found for x{} = {}".format(count, x_ev)
    elif count == max_count:
        results["conclusion"] = "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"
    else:
        results["conclusion"] = "The method exploded"
    
    return results
