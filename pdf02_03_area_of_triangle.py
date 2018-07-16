from math import sqrt

class Coordinate():
   
    def __init__(self,x,y):
        self.x = x
        self.y = y

def side(p1, p2):
    p1x = p1.x
    p1y = p1.y 
    p2x = p2.x
    p2y = p2.y 
    side =  sqrt((p2x-p1x)**2 + (p2y-p1y)**2)
    return side
    
def area_of_triangle(p1, p2, p3):
    s = (side(p1,p2) + side(p2,p3) + side(p1,p3)) / 2
    area = sqrt(s*(s-side(p1,p2))*(s-side(p2,p3))*(s-side(p1,p3)))
    return round(area,2)