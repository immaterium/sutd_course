# Tried to define the class Deque with a dictionary instead of a list
# The dictionary's key indicates the directionality of the data:
#   -Negative keys = items added from the left
#   -Positive keys = items added from the right

class Deque():

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

def is_palindrome(integer):
    integer = str(integer)
    if len(integer) == 1:
        return True
    else:
        integer_list = list(integer)
        myDeque = Deque()
        for each_number in integer_list:
            myDeque.append(each_number)
            left_pos = 0
            right_pos = myDeque.__len__() - 1
        while right_pos >= left_pos:
            if myDeque.__len__() == 1:
                return True
            elif not myDeque.popleft() == myDeque.pop():
                return False
            left_pos += 1
            right_pos -= 1
        return True

print("Test case 1: 1")
ans=is_palindrome(1)
print(ans)

print("Test case 2: 22")
ans=is_palindrome(22)
print(ans)

print("Test case 3: 12321")
ans=is_palindrome(12321)
print(ans)

print("Test case 4: 441232144")
ans=is_palindrome(441232144)
print(ans)

print("Test case 5: 441231144")
ans=is_palindrome(441231144)
print(ans)

print("Test case 6: 144")
ans=is_palindrome(144)
print(ans)

print("Test case 7: 12")
ans=is_palindrome(12)
print(ans)
