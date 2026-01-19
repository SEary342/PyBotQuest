import settings

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
DEFAULT_TAG_COLOR = settings.DARK_GREY
TAG_SPECIFIC_COLORS = {
    1: settings.DARK_BLUE,
    2: settings.DARK_BLUE,
    3: settings.DARK_BLUE,
    4: settings.RED,
    5: settings.RED,
    6: settings.RED,
    7: settings.DARK_BLUE,
    8: settings.RED,
    9: settings.DARK_GREY,
    10: settings.DARK_GREY
}