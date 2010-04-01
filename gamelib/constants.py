
constants = """
SIZE
FILE
FONT
LEVELS
LEVEL_DATA
""".strip()

globs = globals()
for constant in constants.split():
	globs[constant] = constant
