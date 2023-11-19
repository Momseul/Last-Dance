import numpy as np
import math

def f(x):
    return np.log(np.sin(x)**2 + 1) - (1/2)
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
def bisec(a, b, tol):
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
            f(midpoint),
            (current_upper - current_lower) / 2,
            error
        ])
        if (f(midpoint)== 0):
            break
        if isPositive(f(current_lower)) and isPositive(f(midpoint)) or (isNegative(f(current_lower) )and isNegative(f(midpoint))):
            current_lower = midpoint
        else:
            current_upper= midpoint
        old_root= midpoint
    
    root = midpoint
    return results

sol = bisec(0, 1, 1e-7)
print(sol)