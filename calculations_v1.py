import math

def calculate_three_points_route(x1, y1, x2, y2, x3, y3):
    distance1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    distance2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    return round(distance1 + distance2, 2)