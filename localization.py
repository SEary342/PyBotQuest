import math


def calculate_position_from_tag(
    robot_heading, tag_x, tag_y, distance_to_tag, angle_to_tag
):
    """
    Calculates the Robot's (X, Y) position based on a visible tag.

    Concepts:
    1. We know where the Tag is (tag_x, tag_y).
    2. We know how far away it is (distance).
    3. We know the angle to the tag relative to where we are facing.
    """

    # 1. Calculate the absolute angle of the tag in the world
    # We take our current heading and add the angle where we see the tag.
    # (e.g., if we face North (90) and see tag 10 degrees to the right, the tag is at 80).
    absolute_angle_deg = robot_heading + angle_to_tag

    # Convert to radians for Python's math functions
    absolute_angle_rad = math.radians(absolute_angle_deg)

    # 2. Trigonometry Magic
    # If we are at the Robot and the Tag is at 'distance' away:
    # TagX = RobotX + (Distance * cos(angle))
    # Therefore:
    # RobotX = TagX - (Distance * cos(angle))

    estimated_x = tag_x - (distance_to_tag * math.cos(absolute_angle_rad))
    estimated_y = tag_y - (distance_to_tag * math.sin(absolute_angle_rad))
    # Note: We are using Standard Cartesian Coordinates (0,0 is Bottom Left).

    return estimated_x, estimated_y
