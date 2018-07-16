def position_velocity(v0,t):
    G = 9.81
    y = v0 * t - 0.5 * G * (t ** 2)
    y_prime = v0 - G * t
    return round(y,2), round(y_prime,2)

def close_enough(num1, num2):
    to1 = 1e-10
    return abs(num1 - num2) < to1

assert close_enough((position_velocity(5.0,10.0))[0],-440.5) and close_enough((position_velocity(5.0,10.0))[1], -93.1)
assert close_enough((position_velocity(5.0,0.0))[0],0.0) and close_enough((position_velocity(5.0,0.0))[1], 5.0)
assert close_enough((position_velocity(0.0,5.0))[0],-122.62) and close_enough((position_velocity(0.0,5.0))[1], -49.05)
