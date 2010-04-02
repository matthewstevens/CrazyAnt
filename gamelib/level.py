"""

"""

import pygame
import game_object_loader as gol
from camera import Camera

class Level:
	def __init__(self, fp, engine):
		self.player = None
		self.game_objects = []
		self.updatable_objects = []
		self.platforms = pygame.sprite.OrderedUpdates()
		width, height = [int(i) for i in fp.readline().strip().split()]
		objs = gol.load_level(fp.readline().strip())
		for obj in objs:
			obj.setup(self)
		self.game_objects.extend(objs)
		for line in fp:
			line = line.strip()
			obj = gol.load(line)
			obj.setup(self)
			if obj.is_updatable():
				self.updatable_objects.append(obj)
			self.game_objects.append(obj)
		self.camera = Camera(engine, self)
		self.updatable_objects.append(self.camera)

	def update(self, delta):
		for obj in self.updatable_objects:
			obj.update(delta)

	def draw(self, screen):
		self.camera.draw(screen)
		#for obj in self.game_objects:
		#	obj.draw(screen)
			
