from math import sqrt

class Coordinate():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def magnitude(self):
        return sqrt((self.x**2 + self.y**2))
        
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    

p = Coordinate()
assert p.x == 0 and p.y == 0
assert p.magnitude() == 0.0

p.x = 3
p.y = 4
assert p.magnitude() == 5.0

q = Coordinate(3,4)
assert p == q

q.translate(1, 2)
assert q.x == 4

assert p != q