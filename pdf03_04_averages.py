def find_average(list_num):
    n = len(list_num)
    sum_ele = 0
    len_ele = 0
    
    avg_sublist = []
    for sublist in list_num:
        len_sublist = len(sublist)
        sum_sublist = sum(sublist)
        if len(sublist) != 0:
            avg_sublist.append(sum_sublist/len_sublist)
            sum_ele += sum_sublist
            len_ele += len_sublist
        else:
            avg_sublist.append(0)
    all_avg = sum_ele / len_ele
    return(avg_sublist, all_avg)

assert find_average([[3,4],[5,6,7],[-1,2,8]]) == ([3.5, 6.0, 3.0], 4.25)
assert find_average([[13.13,1.1,1.1],[],[1,1,0.67]]) == ([5.11, 0.0, 0.89], 3.0)
assert find_average([[3.6],[1,2,3],[1,1,1]]) == ([3.6 , 2.0 , 1.0] , 1.8)
assert find_average([[2,3,4],[2,6,7],[10,5,15]]) == ([3.0, 5.0, 10.0], 6.0)