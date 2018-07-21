# def sum_cubes(n):
#     sum_cube = 0
#     for i in range(0,n+1):
#         cube = i * i * i
#         sum_cube += cube
#     return (sum_cube)

# print (sum_cubes(3))

def sum_naturals(n):
    term =1
    sum_nat = 0
    while term <= n:
        sum_nat += term
        term += 1
    return sum_nat

def sum_cubes(n):
    term =1
    sum_c = 0
    while term <= n:
        sum_c += term ** 3
        term += 1
    return sum_c

def pi_sum(n):
    term = 1
    sum_pi = 0
    while term <= n:
        sum_pi += 8/((4 * term - 3) * (4 * term - 1))
        term += 1
    return sum_pi

print(sum_naturals(3))
print(sum_cubes(3))
print(pi_sum(3))