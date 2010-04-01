
constants = """
SIZE
FONT
""".strip()

globs = globals()
for constant in constants.split():
	globs[constant] = constant
