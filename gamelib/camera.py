"""
Handles issues with relative positions of game objects relative to the camera
"""
import pygame
from constants import SIZE

class Camera:
	def __init__(self, engine, level):
		game_data = engine.game_data
		self.rect = pygame.Rect((0, 0), game_data[SIZE])
		self.engine = engine
		self.level = level

	def update(self, delta):
		pass

	def draw(self, surface):
		for obj in self.level.game_objects:
			if obj.rect.colliderect(self.rect):
				obj.draw(surface, self)
