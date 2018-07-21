import math

def approx_ode(h, t0, y0, tn):
    no_of_iterations = int((tn - t0) / h)
    x = t0
    y = y0
    for i in range(no_of_iterations):
        y = y + h * (3 + math.e**(-x) - 0.5 * y)
        x = x + h
    return y

## Testing function... ##
print('approx_ode(0.1, 0, 1, 5)')
ans = approx_ode(0.1, 0, 1, 5)
print('Output: ', ans)
print()
print('approx_ode(0.1, 0, 1, 2.5)')
ans = approx_ode(0.1, 0, 1, 2.5)
print('Output: ', ans)
print()
print('approx_ode(0.1, 0, 1, 3)')
ans = approx_ode(0.1, 0, 1, 3)
print('Output: ', ans)
print()
print('approx_ode(0.1, 0, 1, 1) ')
ans = approx_ode(0.1, 0, 1, 1)
print('Output: ', ans)
print()
print('approx_ode(0.1, 0, 1, 0) ')
ans = approx_ode(0.1, 0, 1, 0)
print('Output: ', ans)
