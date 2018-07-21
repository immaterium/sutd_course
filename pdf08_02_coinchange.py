import random
import matplotlib.pyplot as plt
import timeit
import copy
import math

# pseduo code:
# if money is one of (10, 20 ,50, 100)
    # return money
# else
    # for every coin in (10, 20 ,50, 100):
        # if money > coin:
            # remainder = money - coin
            # recursion, call on function again

# def coin_change(money): # T(n)
#     coins_dict = {'10': 0, '20': 0, '50':0, '100':0}
#     coins = [10, 20, 50, 100]
#     if money == 10 or money == 20 or money == 50 or money == 100:
#         return money
#     else:
#         for coin in coins:
#             if money > coin:
#             remainder = money - coin
#             coins_dict[coin] += 1
#             coin_change(remainder)

denoms = [100, 50, 20, 10]

def coin_change(amt):
    if amt == 0:
        return {}
    if amt in denoms:
        return {amt: 1}
    for denom in denoms:
        if amt > denom:
            ret = coin_change(amt-denom)
            if denom in ret:
                ret[denom] += 1
            else:
                ret[denom] = 1
            break
    return ret

print(coin_change(50))
print(coin_change(80))
print(coin_change(120))
print(coin_change(90))