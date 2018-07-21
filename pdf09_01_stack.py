class Stack:

    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self.empty():
            return self._stack.pop()
        else:
            raise IndexError ('Stack is empty.')

    def top(self):
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def empty(self):
        return self.size == 0   


# class Stack:

#     def __init__(self, item):
#         self.item = item
    
#     def pop():
#         pop_item = []
#         self.item[-1] = pop_item
#         del item[-1]

#     def top():
#         item.append(item[0])
#         del item[0]
    
#     def empty():
#         for x in items:
#             if x == None
#             return False
#         else:
#             return True

#     def size():
#         return len(item)
