# lambda syntax
# lambda args: expression

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tol=1e-15):
    return abs(x-y) < tol

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update 


def find_zero(f, df):
    # def update(x):
    #     return x - f(x) / df(x)
    # def near_zero(x):
    #     return approx_eq(f(x), 0)
    return improve(lambda x: x-f(x)/df(x), lambda x: approx_eq(f(x), 0))


def square_root_newton(a):
    def f(x):
        return x**2 - a

    def df(x): 
        return 2 * x

    return find_zero(f, df)

assert square_root_newton(4) == 2.0
assert square_root_newton(16) == 4.0
assert square_root_newton(25) == 5.0


