from math import isclose

def regula_falsi(function, a, b, tol, max_count):
    results = {
        "iterations": [],
        "conclusion": None,
    }
    print("estoy aqui1")
    

    count = 1
    x_r = b - (function(b) * (b - a)) / (function(b) - function(a))
    fx_r = function(x_r)
    error = tol + 1
    temp = 0
    print(a)
    print("estoy aqui2")
    results["iterations"].append([
        count,
        a,
        x_r,
        b,
        fx_r,
        "",
    ])

    while error > tol and count < max_count:
        if fx_r < 0:
            a = x_r
        if fx_r > 0:
            b = x_r
        print(a)

        count += 1
        temp = x_r
        x_r = b - (function(b) * (b - a)) / (function(b) - function(a))
        fx_r = function(x_r)
        error = abs(x_r - temp)

        results["iterations"].append([
            count,
            a,
            x_r,
            b,
            fx_r,
            error,
        ])
        
    if error < tol:
        results["conclusion"] = f"An approximation of the root was found for m = {x_r}"
    elif error > tol:
        results["conclusion"] = "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"
    else:
        results["conclusion"] = "The method exploded"
    return results
