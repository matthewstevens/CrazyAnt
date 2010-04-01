from player import Player
from enemy import Enemy
from tile import Tile

def load(self, line):
	fields = line.split()
	try:
		name = fields[0]
		x = int(fields[1])
		y = int(fields[2])

		if name == "player":
			obj = Player(x, y)
		elif name == "enemy":
			enemy_type = fields[3]
			obj = Enemy(x, y, enemy_type)
		elif name == "tile":
			tile_type = fields[3]
			obj = Tile(x, y, tile_type)
	except IndexError:
		return None
	except ValueError:
		return None

	return obj

