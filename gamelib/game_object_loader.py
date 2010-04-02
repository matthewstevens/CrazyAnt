from player import Player
from enemy import Enemy
from tile import Tile
from constants import *

def load(line):
	fields = line.split()
	try:
		name = fields[0]
		x = int(fields[1])
		y = int(fields[2])
		width = int(fields[3])
		height = int(fields[4])

		if name == PLAYER:
			obj = Player(x, y)
		elif name == ENEMY:
			enemy_type = fields[3]
			obj = Enemy(x, y, enemy_type)
		elif name == TILE:
			tile_type = fields[5]
			obj = Tile(x, y, width, height, tile_type)
	except IndexError:
		print "Received index error, level file does not have correct data field"
		return None
	except ValueError:
		print "Received value error, level file has data not in correct type"
		return None

	return obj

