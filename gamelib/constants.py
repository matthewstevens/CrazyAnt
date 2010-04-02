
constants = """
SIZE
FILE
FONT
LEVELS
LEVEL_DATA
PLAYER
ENEMY
TILE
BRICK
""".strip()

globs = globals()
for constant in constants.split():
	globs[constant] = constant
