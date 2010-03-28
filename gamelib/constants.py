
constants = """
SIZE
""".strip()

globs = globals()
for constant in constants.split():
    globs[constant] = constant
