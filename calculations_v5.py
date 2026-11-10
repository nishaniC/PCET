import math

# Utility function: reusable to calculate the distance between two points.
def get_distance(point_1x, point_1y, point_2x, point_2y):
    if not all(isinstance(i, (int, float)) for i in [point_1x, point_1y, point_2x, point_2y]):
        raise TypeError("All arguments must be numbers")
    return math.sqrt((point_2x - point_1x) ** 2 + (point_2y - point_1y) ** 2)

# Main function that calculates the total distance between three points.
def calculate_three_points_route(x1, y1, x2, y2, x3, y3):
    distance1 = get_distance(x1, y1, x2, y2)
    distance2 = get_distance(x2, y2, x3, y3)
    return round(distance1 + distance2, 2)

# Separate utility function to convert distance into kilometers or miles.
def convert_distance(distance, unit="km"):
    if unit == "km":
        return distance / 1000  # Convert meters to kilometers
    elif unit == "miles":
        return distance * 0.000621371  # Convert meters to miles
    else:
        raise ValueError(f"Unknown unit: {unit}")
