def numbers_with_3(start,end):
    num = start
    while num <= end:
        if '3' in str(num):
            yield num
        num += 1
    
def test_generator_function():
    for num in numbers_with_3(1,1001):
        print(num, end=', ')
        
from timeit import Timer

t1 = Timer("test_generator_function()", "from __main__ import test_generator_function")
# t2 = Timer("test_generator_expression()", "from __main__ import test_generator_expression")

print("Generator function: ",t1.timeit(number=5))
# print("Generator expression: ",t2.timeit(number=5))
