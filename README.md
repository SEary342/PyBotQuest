# PyBotQuest: Robotics Localization Simulator

This project is a 2D simulation designed to teach robotics concepts, specifically **Localization** using visual landmarks (AprilTags). The robot navigates a field, detects tags with a simulated camera, and uses trigonometry to calculate its estimated position on the map.

## Project Structure

Here is a high-level overview of the files in this repository:

*   **`main.py`**: The entry point of the application. It initializes the Pygame window, runs the main simulation loop, handles user input (arrow keys), and manages the drawing of the field, robot, and UI.
*   **`robot_sim.py`**: Defines the `Robot` class. This file handles the "physical" robot, including movement logic, collision detection with walls, and the `scan_for_tags` method which simulates a camera sensor detecting nearby tags.
*   **`localization.py`**: Contains the mathematical logic for determining the robot's position. The function `calculate_position_from_tag` uses the distance and angle to a visible tag to compute the robot's global (X, Y) coordinates.
*   **`Field.py`**: Defines the "World Map". It contains the `KNOWN_TAGS` dictionary, which maps Tag IDs to their absolute (X, Y) coordinates on the field. It also handles tag colors.
*   **`settings.py`**: Stores global constants such as screen dimensions, colors, robot speed, and sensor field-of-view settings.

## Team Goal

**Objective: Align AprilTags with the Game Board**

The current tag coordinates in the simulation do not match the physical layout of our 2026 Rebuilt FRC Field game board.

The team's task is to:
1.  Measure the actual locations of the AprilTags on the physical field.
2.  Update the `KNOWN_TAGS` dictionary in **`Field.py`** with the correct (X, Y) coordinates to ensure the simulation matches reality.

## How to Run

Run the simulation by executing the main script:
`python main.py`
