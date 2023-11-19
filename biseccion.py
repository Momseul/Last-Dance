def isPositive(x):
    if x > 0:
        return True
    else:
        return False
def isNegative(x):
    if x != 0:
        return not isPositive(x)
    else:
        return False
def biseccion_method(equation_lambda, a, b, tol, max_iterations):
    i = 0
    old_root = a
    current_lower= a
    current_upper = b
    error = float('inf')
    results = {"iterations": []}
    while error > tol:
        midpoint = (current_upper + current_lower) / 2
        i += 1
        if midpoint !=0:
            error = abs((midpoint - old_root)/midpoint) ## relative error
            results["iterations"].append([
            i,
            current_lower,
            midpoint,
            current_upper,
            equation_lambda(midpoint),
            (current_upper - current_lower) / 2,
            #error
        ])
        if (equation_lambda(midpoint)== 0):
            break
        if isPositive(equation_lambda(current_lower)) and isPositive(equation_lambda(midpoint)) or (isNegative(equation_lambda(current_lower) )and isNegative(equation_lambda(midpoint))):
            current_lower = midpoint
        else:
            current_upper= midpoint
        old_root= midpoint
    
    if error < tol:
        results["conclusion"] = f"An approximation of the root was found for m = {midpoint}"
    elif error > tol:
        results["conclusion"] = "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"
    else:
        results["conclusion"] = "The method exploded"
    return results