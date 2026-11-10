import pytest
from calculations_v5 import get_distance,calculate_three_points_route, convert_distance
"""
file and tests  has to start with test_
for pytest to discover them
"""
def test_calculate_three_points_route():
    # Arrange: Define the coordinates for the points
    start_point = (0, 0)
    middle_point = (3, 4)
    finish_point = (4, 3)
    expected_result = 6.41

    # Act: Call the existing function
    result = calculate_three_points_route(start_point[0], start_point[1], middle_point[0], middle_point[1],
                                          finish_point[0], finish_point[1])

    # Assert: Check if the result matches the expected output (6.41)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'


def test_convert_distance():
    # Arrange: Define a sample distance in meters.
    distance_in_meters = 6410  # Example distance

    # Act & Assert: Convert the distance to kilometers.
    km_result = convert_distance(distance_in_meters, "km")
    assert km_result == distance_in_meters / 1000, f"Expected {distance_in_meters / 1000} km, but got {km_result}"

    # Act & Assert: Convert the distance to miles.
    miles_result = convert_distance(distance_in_meters, "miles")
    expected_miles = distance_in_meters * 0.000621371
    assert round(miles_result, 8) == round(expected_miles,8), f"Expected {expected_miles} miles, but got {miles_result}"


def test_calculate_four_points_route_type_error1():
    # Arrange: Define the valid coordinates for the points.
    start_point = (0, 0)
    middle_point = (3, 4)
    finish_point = (4, 3)

    # Act & Assert: Call the function with valid input and check the result.
    result = calculate_three_points_route(start_point[0], start_point[1], middle_point[0], middle_point[1],
                                          finish_point[0], finish_point[1])
    assert result == 6.41, f'Incorrect value: expected 6.41 but got {result}'

    # Act & Assert: Ensure the error is raised when passing invalid input.
    try:
        get_distance(start_point[0], start_point[1], 'invalid', None)
    except TypeError as e:
        print(f"Error caught: {e}")  # Expected output: "All arguments must be numbers"

"""
Test the exception type → pytest.raises(TypeError)
Test the exception type and message → pytest.raises(TypeError, match="...")
"""
def test_calculate_three_points_route_type_error():
    with pytest.raises(TypeError, match="All arguments must be numbers"):
        calculate_three_points_route(
            "0", 0,
            3, 4,
            4, 3
        )

@pytest.mark.parametrize("bad_value", ["0", None, [], {}])
def test_calculate_three_points_route_type_errors(bad_value):
    with pytest.raises(TypeError, match="All arguments must be numbers"):
        calculate_three_points_route(
            bad_value, 0,
            3, 4,
            4, 3
        )


def test_convert_distance_unknown_unit1():
    try:
        convert_distance(1000, "unknown_unit")
    except ValueError as e:
        print(f"Error caught: {e}")  # Expected output: "Unknown unit: unknown_unit"

def test_convert_distance_unknown_unit():
    with pytest.raises(ValueError, match="Unknown unit: cm"):
        convert_distance(
            1000, "cm"
        )