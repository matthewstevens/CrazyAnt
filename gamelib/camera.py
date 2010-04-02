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
		if self.level.player.rect.centerx > self.rect.centerx+64:
			self.rect.centerx = self.level.player.rect.centerx-64
		if self.level.player.rect.centerx < self.rect.centerx-64:
			self.rect.centerx = self.level.player.rect.centerx+64
		if self.level.player.rect.centery > self.rect.centery+128:
			self.rect.centery = self.level.player.rect.centery-128
		if self.level.player.rect.centery < self.rect.centery-64:
			self.rect.centery = self.level.player.rect.centery+64
		

	def draw(self, surface):
		for obj in self.level.game_objects:
			if obj.rect.colliderect(self.rect):
				obj.draw(surface, self)
