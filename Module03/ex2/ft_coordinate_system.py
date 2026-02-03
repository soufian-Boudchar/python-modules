import math


def calculate_distance(p1, p2):
    """
    Calculates the 3D Euclidean distance between two points.

    Args:
        p1 (tuple): The first point (x, y, z).
        p2 (tuple): The second point (x, y, z).

    Returns:
        float: The distance between p1 and p2.
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def main():
    """
    Main function to execute the coordinate system demonstration.
    """
    print("=== Game Coordinate System ===")

    pos1 = (10, 20, 5)
    origin = (0, 0, 0)

    print(f"Position created: {pos1}")

    dist = calculate_distance(pos1, origin)
    print(f"Distance between {origin} and {pos1}: {dist:.2f}\n")

    parse_str = "3,4,0"
    print(f'Parsing coordinates: "{parse_str}"')

    try:
        parsed_pos = tuple(int(i) for i in parse_str.split(','))

        print(f"Parsed position: {parsed_pos}")

        dist2 = calculate_distance(parsed_pos, origin)
        print(f"Distance between {origin} and {parsed_pos}: {dist2}\n")

    except ValueError:
        print("Error: Could not parse valid coordinates.\n")

    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')

    try:
        tuple(int(i) for i in invalid_str.split(','))
    except ValueError as err:
        print(f"Error parsing coordinates: {err}")
        print(
            f"Error details - Type: {type(err).__name__}, Args: {err.args}\n")

    print("Unpacking demonstration:")

    x, y, z = parsed_pos

    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
