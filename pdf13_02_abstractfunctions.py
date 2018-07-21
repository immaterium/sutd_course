
# def sum_naturals(n):
#     term =1
#     sum_nat = 0
#     while term <= n:
#         sum_nat += term
#         term += 1
#     return sum_nat

# def sum_cubes(n):
#     term =1
#     sum_c = 0
#     while term <= n:
#         sum_c += term ** 3
#         term += 1
#     return sum_c

# def pi_sum(n):
#     term = 1
#     sum_pi = 0
#     while term <= n:
#         sum_pi += 8/((4 * term - 3) * (4 * term - 1))
#         term += 1
#     return sum_pi

def summation(n, term_func):
    result = 0
    term = 1
    while term <= n:
        result += term_func(term)
        term += 1
    return result

def cubes(x):
    return x ** 3

def pi(x):
    return 8/((4 * x - 3) * (4 * x - 1))

def naturals(x):
    return x

print(summation(3,naturals))
print(summation(3,cubes))
print(summation(3,pi))


# print(sum_naturals(3))
# print(sum_cubes(3))
# print(pi_sum(3))