import dudraw
import random
from math import sqrt

"""
This file will run the brute force version of the algorithm
"""

# this controls the number of points created
point_number = 20


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def draw(self):
        dudraw.filled_circle(self.x,self.y,0.01)
    

class Edge(Point):
    def __init__(self, point1, point2):
        super().__init__(point1.x, point1.y)
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return f"Edge({self.point1}, {self.point2})"

    def __repr__(self):
        return f"Edge({self.point1}, {self.point2})"

    def draw(self):
        dudraw.line(self.point1.x, self.point1.y, self.point2.x, self.point2.y,)

def findDistance(one: Point, two: Point):
    return sqrt((one.x - two.x)**2 + (one.y - two.y)**2)





def pointsBrute(P: list):
    #even if the two points were one the very diagonal, 1.5 is still farther, and a good upper bound
    lowest = 1.5
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            distance = findDistance(P[i], P[j])
            if distance < lowest:
                point_1 = P[i]
                point_2 = P[j]
                lowest = distance
    return [Edge(point_1, point_2), lowest]



dudraw.set_pen_width(.006)
points = []
for i in range(point_number):
    points.append(Point(random.random(),random.random()))
for point in points:
    point.draw()

result = pointsBrute(points)
edge = result[0]

dudraw.set_pen_color(dudraw.RED)
edge.draw()
dudraw.show(10000)



  
