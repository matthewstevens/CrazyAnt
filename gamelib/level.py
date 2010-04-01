
import game_object_loader as gol

class Level:
	def __init__(self, fp):
		self.game_objects = []
		for line in fp:
			line = line.strip()
			obj = gol.load(line)
			self.game_objects.append(obj)

	def draw(self):
		for obj in self.game_objects:
			obj.draw()
			
