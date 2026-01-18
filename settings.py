# Screen settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FPS = 60

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
DARK_BLUE = (0, 0, 139)
LIGHT_RED = (255, 220, 220)
LIGHT_BLUE = (220, 220, 255)
DARK_GREY = (51, 51, 51)


# Robot Settings
ROBOT_SIZE = 30
ROBOT_SPEED = 3
ROTATION_SPEED = 3

# SENSOR SETTINGS
# How far the robot can "see" a tag (in pixels)
MAX_DETECTION_DISTANCE = 200 
# Field of view (in degrees)
FOV = 90 

# THE MAZE DATA
# "2026 Rebuilt FRC Field" Layout
# Format: ID: (x_position, y_position)
KNOWN_TAGS = {
    # Blue Alliance Wall (Left)
    1: (50, 450),
    2: (50, 300),
    3: (50, 150),
    # Red Alliance Wall (Right)
    4: (1150, 450),
    5: (1150, 300),
    6: (1150, 150),
    # Central Structure (The "Core")
    7: (550, 300),
    8: (650, 300),
    9: (600, 350),
    10: (600, 250)
}

# Tag Appearance
DEFAULT_TAG_COLOR = DARK_GREY
TAG_SPECIFIC_COLORS = {
    1: DARK_BLUE,
    2: DARK_BLUE,
    3: DARK_BLUE,
    4: RED,
    5: RED,
    6: RED,
    7: DARK_BLUE,
    8: RED,
    9: DARK_GREY,
    10: DARK_GREY
}