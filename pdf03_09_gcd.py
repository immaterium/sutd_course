def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
        # a divides by b to give remainder
        # this remainder is now (the new value) b 
        # a takes on the old value of b
        # loop this as long as b exist
        # the value of a%b will eventually reach 0 under this Euclidean Algorithm
        # and the loop will terminate here to give the GCD as the value of final a
        # use pythontutor.com to see
    return a

assert gcd(36, 9) == 9