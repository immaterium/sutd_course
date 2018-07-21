import random
import matplotlib.pyplot as plt
import timeit
import copy
import math

# def insertion_sort(list_items):
#    list_items = copy.copy(list_items) 
#    for index in range(1, len(list_items)): # theta (n-1)
#        cur_val = list_items[index] # theta(1)
#        position = index # theta(1)
       
#     while position > 0 and list_items[position -1] > cur_val: # worst case theta(n-1)
#         list_items[position] = list_items[position - 1]       # theta(1)
#         position -= 1                                         # theta(1)

#         list_items[position] = cur_val                           # theta(1)
#     return list_items

def insertion_sort(list_items):
   list_items = copy.copy(list_items)
   for index in range(1, len(list_items)):
       cur_val = list_items[index]
       position = index
       
       while position > 0 and list_items[position -1] > cur_val:
           list_items[position] = list_items[position - 1]
           position -= 1
       list_items[position] = cur_val
   return list_items

assert insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]

preparation_insertion = """
import random
from __main__ import insertion_sort
"""


data ="""
items = list(range({}))
random.shuffle(items)
"""

preparation_sort = """
import random
"""
x_axis = [10**n for n in range(1,5)]
data_list = [data.format(x) for x in x_axis]

insertion_time = []
sort_time = []

for x in range(len(x_axis)):
	t = timeit.Timer("insertion_sort(items)",preparation_insertion + data_list[x])
	insertion_time.append(t.timeit(number=1))
	t = timeit.Timer("sorted(items)",preparation_sort + data_list[x])
	sort_time.append(t.timeit(number=1))

print(insertion_time)
print(sort_time)

# 2 rows, 1 column, put into first plot
# y = x^2 for each x

plt.subplot(2,1,1)
x2_axis = [x*x for x in x_axis]
plt.plot (x2_axis, insertion_time, 'o-')

plt.subplot(2,1,2)
xlogx_axis = [x*math.log(x) for x in x_axis]
plt.plot (xlogx_axis, sort_time, 'o-')

plt.show()

# import random
# import time

# def random_ints(num, lower=0, upper=9):
#     return [random.randrange(lower,upper+1) for i in range(num)]
 
# def insertionSort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue


# alist = random_ints(10)
# insertionSort(alist)
# print(alist)

# alist = random_ints(100)
# insertionSort(alist)
# print(alist)

# alist = random_ints(1000)
# insertionSort(alist)
# print(alist)

# alist = random_ints(10000)
# insertionSort(alist)
# print(alist)