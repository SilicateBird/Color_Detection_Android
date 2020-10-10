import math

# pythagorean_distance
def pytha(point1, point2):
    return math.hypot(point2[0] - point1[0], point2[1] - point1[1])

# find distance from pointO to vertices of triangle ABC
def triangle_distance(pointO, pointA, pointB, pointC):
    return [pytha(pointA, pointO), pytha(pointB, pointO), pytha(pointC, pointO)]

var = triangle_distance([1, 2], [2, 3], [5,-1], [2, 1])
print(var)