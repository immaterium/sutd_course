def add_powers(n):
    def sum_powers(list_num):
        return sum ([x ** n for x in list_num])
    return sum_powers

series1 = [0, 1, 2, 3, 4, 5]
series2 = [2, 4, 8, 16, 32]

power_reducer = add_powers (2)
print(power_reducer(series1))
print(power_reducer(series2))

power_reducer = add_powers (3)
print(power_reducer(series1))
print(power_reducer(series2))