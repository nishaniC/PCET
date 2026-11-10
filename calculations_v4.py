import math

# Refactored function with error handling added.
def get_distance(point_1x, point_1y, point_2x, point_2y):
    if not all(isinstance(i, (int, float)) for i in (point_1x, point_1y, point_2x, point_2y)):
        raise TypeError("All arguments must be numbers")
    return math.sqrt((point_2x - point_1x) ** 2 + (point_2y - point_1y) ** 2)

# Main function remains focused on calculating the total distance.
def calculate_three_points_route(x1, y1, x2, y2, x3, y3):
    distance1 = get_distance(x1,y1,x2,y2)
    distance2 = get_distance(x2,y2,x3,y3)
    return round(distance1 + distance2, 2)