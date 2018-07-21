# visualise on pythontutor
# understand time taken

import random
import matplotlib.pyplot as plt
import timeit
import copy
import math

# T(n) = theta(1) + theta(n/2) + 2 theta(n/2) + theta(n)
# = theta(n) + 2 theta(n/2)
# = c.n + 2 theta(n/2)

# visualise tree
# there will be n leaves
# height = 1 + log2n

# summation i=0 to 1+log2n (cn)
# will be cn + cnlog2n
# and be theta(nlog2n) because cnlog2n will dominate effect on the graph


def merge_sort(items): # T(n)
    len_items = len(items)
    if len_items > 1:
        mid_pos = len_items//2 # theta(1)
        left_items = items[:mid_pos] # theta(n/2)
        right_items = items[mid_pos:] # thera(n/2)

        merge_sort(left_items) # T(n/2)
        merge_sort(right_items) # T(n/2)

        left_idx = 0
        right_idx = 0
        out_idx = 0
	
        len_left = len(left_items)
        len_right = len(right_items)
        
        while left_idx < len_left and right_idx < len_right: # theta(n) because merging everything until n elements
            if left_items[left_idx] < right_items[right_idx]:
                items[out_idx] = left_items[left_idx]
                left_idx += 1
            else:
                items[out_idx] = right_items[right_idx]
                right_idx += 1
            out_idx +=1

        while left_idx < len_left:
            items[out_idx] = left_items[left_idx]
            left_idx += 1
            out_idx += 1
	
        while right_idx < len_right:
            items[out_idx] = right_items[right_idx]
            right_idx += 1
            out_idx += 1

list_a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(list_a)
print(list_a)

# assert merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]

preparation_merge = """
import random
from __main__ import merge_sort
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

merge_time = []
sort_time = []

for x in range(len(x_axis)):
	t = timeit.Timer("merge_sort(items)",preparation_merge + data_list[x])
	merge_time.append(t.timeit(number=1))
	t = timeit.Timer("sorted(items)",preparation_sort + data_list[x])
	sort_time.append(t.timeit(number=1))

print(merge_time)
print(sort_time)

# 2 rows, 1 column, put into first plot
# y = x^2 for each x

plt.subplot(2,1,1)
x_axis1 = [x for x in x_axis]
plt.plot (x_axis1, merge_time, 'o-')

plt.subplot(2,1,2)
x_axis2 = [x for x in x_axis]
plt.plot (x_axis2, sort_time, 'o-')

plt.show()

# plt.subplot(2,1,1)
# x2_axis = [x*x for x in x_axis]
# plt.plot (x2_axis, merge_time, 'o-')

# plt.subplot(2,1,2)
# xlogx_axis = [x*math.log(x) for x in x_axis]
# plt.plot (xlogx_axis, sort_time, 'o-')