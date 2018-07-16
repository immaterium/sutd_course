import pdf02_03_area_of_triangle as tri
import math

class Coordinate():
   
    def __init__(self,x,y):
        self.x = x
        self.y = y

# print("Test Case 1") 
# p1=Coordinate(1.5, -3.4) 
# p2=Coordinate(4.6, 5) 
# p3=Coordinate(9.5, -3.4)
# ans=tri.area_of_triangle(p1,p2,p3) 
# print(ans)

# print("Test Case 2") 
# p1=Coordinate(2.0, -3.4) 
# p2=Coordinate(4.6, 5) 
# p3=Coordinate(9.5, -1.4)
# ans=tri.area_of_triangle(p1,p2,p3) 
# print(ans)

# print("Test Case 3") 
# p1 = Coordinate(1.5, 3.4) 
# p2 = Coordinate(4.6, 5) 
# p3 = Coordinate(-1.5, 3.4) 
# ans = tri.area_of_triangle(p1,p2,p3)
# print(ans)

# print("Test Case 4") 
# p1=Coordinate(-1.5, 3.4) 
# p2=Coordinate(4.6, 5) 
# p3=Coordinate(4.3, -3.4)
# ans=tri.area_of_triangle(p1,p2,p3) 
# print(ans)


p1x = float(input('Enter x coordinate of the first point of a triangle: '))
p1y = float(input('Enter y coordinate of the first point of a triangle: '))
p2x = float(input('Enter x coordinate of the second point of a triangle: '))
p2y = float(input('Enter y coordinate of the second point of a triangle: '))
p3x = float(input('Enter x coordinate of the third point of a triangle: '))
p3y = float(input('Enter y coordinate of the third point of a triangle: '))

p1=Coordinate(p1x, p1y) 
p2=Coordinate(p2x, p2y) 
p3=Coordinate(p3x, p3y)
ans=tri.area_of_triangle(p1,p2,p3) 
print(ans)