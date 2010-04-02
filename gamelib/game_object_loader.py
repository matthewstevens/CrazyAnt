from player import Player
from enemy import Enemy
from tile import Tile
from constants import *
from pygame import image
from util import file_path

def load(line):
	fields = line.split()
	try:
		name = fields[0]
		x = int(fields[1])
		y = int(fields[2])

		if name == PLAYER:
			obj = Player(x, y)
		elif name == ENEMY:
			enemy_type = fields[3]
			obj = Enemy(x, y, enemy_type)
		elif name == TILE:
			tile_type = fields[3]
			obj = Tile(x, y, tile_type)
	except IndexError:
		print "Received index error, level file does not have correct data field"
		return None
	except ValueError:
		print "Received value error, level file has data not in correct type"
		return None

	return obj

def load_level(file_name):
	level = image.load(file_path(file_name))
	tiles = []
	for y in range(level.get_height()):
		for x in range(level.get_width()):
			colour = level.get_at((x, y))
			if colour == (0, 0, 0, 0):
				tiles.append(Tile(x, y, "BRICK"))
	return tiles
