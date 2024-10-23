import dudraw
import random
import math

"""
This file will run a for loop that will continuously generate random points and run the brute force
and then divide and conquer methods, showing their identical results.
"""

# this controls the number of points created
point_number = 40

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
    return math.sqrt((one.x - two.x)**2 + (one.y - two.y)**2)

def merge_sort_x(A = list, p = int, r = int):
    if p == r:
        return
    else:
        q = (p + r)//2
        merge_sort_x(A, p, q)
        merge_sort_x(A, q + 1, r)
        merge_x(A, p, q, r)

def merge_x(A = list, p = int, q = int, r = int):
    sub_1_length = q - p + 1
    sub_2_length = r - q
    right = []
    left = []
    for i in range(sub_1_length):
        left.append(A[p + i])
    for j in range(sub_2_length):
        right.append(A[q + j + 1])

    i = 0
    j = 0
    for k in range(p, r+1):
        if i > len(left)-1:
            A[k] = right[j]
            j = j + 1
        
        elif j > len(right)-1 or left[i].x <= right[j].x:
            A[k] = left[i]
            i = i + 1
        else:
            A[k] = right[j]
            j = j + 1


def merge_sort_y(A = list, p = int, r = int):
    if p == r:
        return
    else:
        q = (p + r)//2
        merge_sort_y(A, p, q)
        merge_sort_y(A, q + 1, r)
        merge_y(A, p, q, r)

def merge_y(A = list, p = int, q = int, r = int):
    sub_1_length = q - p + 1
    sub_2_length = r - q
    right = []
    left = []
    for i in range(sub_1_length):
        left.append(A[p + i])
    for j in range(sub_2_length):
        right.append(A[q + j + 1])

    i = 0
    j = 0
    for k in range(p, r+1):
        if i > len(left)-1:
            A[k] = right[j]
            j = j + 1
        
        elif j > len(right)-1 or left[i].y <= right[j].y:
            A[k] = left[i]
            i = i + 1
        else:
            A[k] = right[j]
            j = j + 1

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




def pointsDivide(P:list, X:list, Y:list):
    if len(P) <= 3:
        return pointsBrute(list(P))

    X_L = X[:len(X)//2]
    X_R = X[len(X)//2:]
    line = X_R[0].x - (X_R[0].x - X_L[-1].x)/2
    P_L = set(X_L)
    P_R = set(X_R)
    Y_L = []
    Y_R = []
    for i in range(len(Y)):
        if Y[i] in P_L:
            Y_L.append(Y[i])
        elif Y[i] in P_R:
            Y_R.append(Y[i])
        else:
            print("THIS SHOULD NEVER EVER RUN BRUH.")
    
     # 1 subscropt becuase the brute force return format
    min_left = pointsDivide(P_L,X_L,Y_L)
    min_right = pointsDivide(P_R,X_R,Y_R)
    if min_right[1] <= min_left[1]:
        minn = min_right[1]
        min_returnable = min_right
    else:
       minn = min_left[1]
       min_returnable = min_left

    Y_prime = []
    for point in Y:
        distance_from_line = abs(line - point.x)
        # dudraw.line(line,1,line,0)
        # point.draw()
        # dudraw.show(10)
        if distance_from_line < minn:
            Y_prime.append(point)

    minn_prime = minn
    for i in range(len(Y_prime)):
        for j in range(i+1,i+7):
            if j > len(Y_prime)-1:
                # OR CONTINUE IDK
                break
            minn_prime = findDistance(Y_prime[i],Y_prime[j])
            if minn_prime < minn:
                minn = minn_prime
                min_returnable = [Edge(Y_prime[i],Y_prime[j]), minn_prime]


    return min_returnable



def pointsDivideStart(P:set):
    X = []
    Y = []
    for point in P:
        X.append(point)
        Y.append(point)
    merge_sort_x(X,0,point_number-1)
    merge_sort_y(Y,0,point_number-1)

    return pointsDivide(P,X,Y)




dudraw.set_font_size(100)
dudraw.set_pen_width(.006)
for i in range(10000):

    points = set()
    for i in range(point_number):
        points.add(Point(random.random(),random.random()))

    edge1 = pointsBrute(list(points))[0]
    edge2 = pointsDivideStart(points)[0]
    
    dudraw.set_font_size(100)
    dudraw.text(.5,.5,"BRUTE")
    dudraw.show(1000)
    dudraw.clear()
    for point in points:
        point.draw()
    dudraw.show(1000)
    dudraw.set_pen_color(dudraw.RED)
    edge1.draw()
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.show(1000)
    dudraw.clear()
    dudraw.text(.5,.5,"DIVIDE")
    dudraw.show(1000)
    dudraw.clear()
    for point in points:
        point.draw()
    dudraw.show(1000)
    dudraw.set_pen_color(dudraw.RED)
    edge2.draw()
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.show(1000)
    dudraw.clear()






        
        



    















