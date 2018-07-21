def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1+1/guess

def square_close_to(guess):
    sq = guess*guess
    return approx_eq(sq, guess+1)

def approx_eq(x, y, tol=1e-15):
    return abs(x-y) < tol

print(improve(golden_update, square_close_to))
