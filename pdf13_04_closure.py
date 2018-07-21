def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def calculate_phi(tolerance):
    def golden_update(guess):
        return 1+1/guess

    def square_close_to(guess):
        sq = guess*guess
        return approx_eq(sq, guess+1, tolerance)
    return improve(golden_update, square_close_to)

def approx_eq(x, y, tol=1e-15):
    return abs(x-y) < tol

# print(improve(golden_update, square_close_to))

print(calculate_phi(1e-10) )