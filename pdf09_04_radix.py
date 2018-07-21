from pdf09_03_queue import Queue

def radix_sort(items):
    main_bin = Queue()
    radix_bin = {str(x): Queue() for x in range(10)}

    max_iter = max([len(str(x)) for x in items])
    digit = 0
    for item in items:
        main_bin.put(item)

    while digit < max_iter:

        while not main_bin.empty():
            item = main_bin.get()
            str_item = str(item)
            try:
                digit_interest = str_item[-1-digit]
                radix_bin[digit_interest].put(item)
            except IndexError:
                radix_bin['0'].put(item)

        for (key, val) in sorted(zip(radix_bin.keys(), radix_bin.values())):
            while not radix_bin[key].empty():
                item = radix_bin[key].get()
                main_bin.put(item)
        digit += 1
    return main_bin
    
items = [54, 26, 94, 17, 77, 31, 44, 55, 20, 65]
result = radix_sort(items)
resultlist = [result.get() for x in range(result.qsize())] 
assert resultlist == [17, 20, 26, 31, 44, 54, 55, 65, 77, 94]


# class Queue:

#     def __init__(self):
#         self._queue = []

#     def put(self, item):
#         self._queue.append(item)

#     def get(self):
#         return self._queue[0]

#     def qsize(self):
#         return len(self._queue)

#     def empty(self):
#         return self.qsize == 0   

#     def radix_sort(self,digits):
        
#         main_bin = Queue()
#         zero_bin = Queue()
#         one_bin = Queue()
#         two_bin = Queue()
#         three_bin = Queue()
#         four_bin = Queue()
#         five_bin = Queue()
#         six_bin = Queue()
#         seven_bin = Queue()
#         eight_bin = Queue()
#         nine_bin = Queue()

#         for digit in digits:
#             digit = str(digit)
#             return digits


        


