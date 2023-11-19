from sympy import symbols, lambdify

def fixed_point_method(f, g, x0, tol, max_count):
    error = 0
    count = 0
    xN = 0

    fX = f(x0)
    results = {
        "iterations": [],
        "conclusion": None
    }

    xN = g(x0)
    
    results["iterations"].append([
        count,
        x0,
        xN,
        fX,
        None
    ])
    
    error = abs(x0 - xN)
    fX = f(xN)
    
    while error > tol and count < max_count and fX != 0:
        x0 = xN
        xN = g(x0)
        count += 1
        results["iterations"].append([
            count,
            x0,
            xN,
            fX,
            error
        ])
        error = abs(x0 - xN)
        fX = f(xN)
    
    if fX == 0:
        x0 = xN
        xN = g(x0)
        count += 1
        results["iterations"].append([
            count,
            x0,
            xN,
            fX,
            error
        ])
        results["conclusion"] = "The root was found for xN = {}".format(x0)
        return results
    elif error <= tol:
        x0 = xN
        xN = g(x0)
        count += 1
        results["iterations"].append([
            count,
            x0,
            xN,
            fX,
            error
        ])
        results["conclusion"] = "An approximation of the root was found for xN = {}".format(x0)
        return results
    elif count == max_count:
        results["conclusion"] = "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"
        return results
    else:
        results["conclusion"] = "The method exploded"
        return results
