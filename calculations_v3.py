import math

# DRY principle applied: a reusable function to calculate the distance between two points.
def get_distance(point_1x, point_1y, point_2x, point_2y):
    return math.sqrt((point_2x - point_1x) ** 2 + (point_2y - point_1y) ** 2)

# Refactored function using the DRY principle.
def calculate_three_points_route(x1, y1, x2, y2, x3, y3):
    distance1 = get_distance(x1,y1,x2,y2)
    distance2 = get_distance(x2,y2,x3,y3)
    return round(distance1 + distance2, 2)