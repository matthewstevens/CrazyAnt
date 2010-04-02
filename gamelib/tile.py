from game_object import GameObject
from util import load

class Tile(GameObject):
	def __init__(self, x, y, width, height, tile_type):
		super(Tile, self).__init__(x, y, width, height)


