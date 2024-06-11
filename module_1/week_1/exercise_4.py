def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

def approx_sin(x: float, n: int):
    sin_x = 0
    for i in range(n):
        sign = (-1) ** i
        sin_x += sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)

    return sin_x

def approx_cos(x: float, n: int):
    cos_x = 0
    for i in range(n):
        sign = (-1) ** i
        cos_x += sign * (x ** (2 * i)) / factorial(2 * i)

    return cos_x

def approx_sinh(x: float, n: int):
    sinh_x = 0
    for i in range(n):
        sinh_x += (x ** (2 * i + 1)) / factorial(2 * i + 1)

    return sinh_x

def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        cosh_x += (x ** (2 * i)) / factorial(2 * i)

    return cosh_x

if __name__ == "__main__":
    x = 3.14
    n = 10
    print(f"sin({x}) = {approx_sin(x, n)}")
    print(f"cos({x}) = {approx_cos(x, n)}")
    print(f"sinh({x}) = {approx_sinh(x, n)}")
    print(f"cosh({x}) = {approx_cosh(x, n)}")
