"""

"""
import pygame
from util import relative_rect

class GameObject(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super(GameObject, self).__init__()
		self.rect = pygame.Rect(
			x,# - (width / 2.0),
			y,# - (height / 2.0),
			width,
			height
		)
	def setup(self, level):
		pass
	def is_updatable(self):
		return False
	def draw(self, screen, camera):
		rel_rect = relative_rect(self.rect, camera.rect)
		screen.fill((255,255,255), rel_rect)
