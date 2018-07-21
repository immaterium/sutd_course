# Tried to define the class Deque with a dictionary instead of a list
# The dictionary's key indicates the directionality of the data:
#   -Negative keys = items added from the left
#   -Positive keys = items added from the right

class Deque(object):

    def __init__(self):
        # initialise with default values
        self.left = self.right = 0
        self.data = {}
        self.maxsize = -1

    def append(self, x):
        self.data[self.right] = x
        self.right += 1
        if self.maxsize != -1 and len(self) > self.maxsize:
            self.popleft()

    def appendleft(self, x):
        self.left -= 1
        self.data[self.left] = x
        if self.maxsize != -1 and len(self) > self.maxsize:
            self.pop()

    def pop(self):
        if self.left == self.right:
            raise IndexError('Deque is empty')
        self.right -= 1
        elem = self.data[self.right]
        del self.data[self.right]
        return elem

    def popleft(self):
        if self.left == self.right:
            raise IndexError('Deque is empty')
        elem = self.data[self.left]
        del self.data[self.left]
        self.left += 1
        return elem

    def __len__(self):
        return len(self.data)

## Testing... ##
myDeque = Deque()

myDeque.append(1)
assert myDeque.data == {0: 1}

myDeque.appendleft(2)
assert myDeque.data == {0: 1, -1: 2}

myDeque.appendleft(3)
assert myDeque.data == {0: 1, -1: 2, -2: 3}

myDeque.append(5)
assert myDeque.data == {0: 1, -1: 2, -2: 3, 1: 5}

assert myDeque.__len__() == 4

myDeque.popleft()
assert myDeque.data == {0: 1, -1: 2, 1: 5}

myDeque.pop()
assert myDeque.data == {0: 1, -1: 2}
