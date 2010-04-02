from game_object import GameObject

class Player(GameObject):
	def __init__(self, x, y):
		super(Player, self).__init__(x*40, y*40, 40, 40)
	def update(self, delta):
		pass
	def is_updatable(self):
		return True
	def setup(self, level):
		self.level = level
