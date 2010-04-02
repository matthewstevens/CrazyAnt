"""

"""
import pygame

class GameObject(object):
	def __init__(self, x, y, width, height):
		self.rect = pygame.Rect(
			x - (width / 2.0),
			y - (height / 2.0),
			width,
			height
		)
	def draw(self, screen):
		screen.fill((255,255,255), self.rect)


