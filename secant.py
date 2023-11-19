
def secant_method(f, x0, x1, tol, max_count):
    error = 0
    count = 0
    
    fX0 = f(x0)
    fX1 = f(x1)
    xN = x1 - (fX1 * (x1 - x0)) / (fX1 - fX0)
    fXN = f(xN)
    
    results = {
        "iterations": [],
        "conclusion": None
    }
    
    if f(x0).imag:
        raise ValueError("x0 isn't defined in the domain of the function f: x0 = {}".format(x0))
    if max_count < 0:
        raise ValueError("Max iterations is < 0: iterations = {}".format(max_count))
    if tol < 0:
        raise ValueError("tol is an incorrect value: tol = {}".format(tol))
    if x0 == x1:
        raise ValueError("x0 is equal to x1: x0 = {} ^ x1 = {}".format(x0, x1))
    
    results["iterations"].append([
        count,
        x0,
        fX0,
        None
    ])
    
    if fX0 == 0:
        results["conclusion"] = "x{} is the root: {}".format(count, x0)
        return results
    
    count += 1
    
    results["iterations"].append([
        count,
        x1,
        fX1,
        None
    ])
    
    if fX1 == 0:
        results["conclusion"] = "x{} is the root: {}".format(count, x1)
        return results
    
    count += 1
    error = abs(x1 - xN)
    
    results["iterations"].append([
        count,
        xN,
        fXN,
        error
    ])
    
    if fXN == 0:
        results["conclusion"] = "x{} is the root: {}".format(count, xN)
        return results
    
    while error > tol and count < max_count and fXN != 0:
        x0 = x1
        x1 = xN
        fX0 = f(x0)
        fX1 = f(x1)
        
        if fX1 - fX0 != 0:
            xN = x1 - (fX1 * (x1 - x0)) / (fX1 - fX0)
            error = abs(x1 - xN)
            count += 1
            
            results["iterations"].append([
                count,
                xN,
                fXN,
                error
            ])
        else:
            results["conclusion"] = ("The denominator is 0, the method cannot be continued. "
                                     "The last approximate root found is {} with an error of {}"
                                     .format(xN, error))
            return results
    
    if fXN == 0:
        results["conclusion"] = "The root was found for xN = {}".format(xN)
    elif error <= tol:
        results["conclusion"] = "An approximation of the root was found for x{} = {}".format(count, xN)
    elif count == max_count:
        results["conclusion"] = ("Given the number of iterations and the tolerance, "
                                  "it was impossible to find a satisfying root")
    else:
        results["conclusion"] = "The method exploded"
    
    return results
