from game_object import GameObject
from util import load

class Tile(GameObject):
	def __init__(self, x, y, tile_type):
		super(Tile, self).__init__(x* 40, y * 40, 40, 40)
	def setup(self, level):
		self.add(level.platforms)


