import pygame
from game_object import GameObject
from util import Vector

gravity = Vector(x=0, y=1)
left = Vector(x=-2, y = 0)
right = Vector(x=2, y = 0)
up = Vector(x=0, y = -20)
down = Vector(x=0, y = 2)

class Player(GameObject):
	def __init__(self, x, y):
		super(Player, self).__init__(x*40, y*40, 40, 40)
		self.velocity = Vector()
		self.terminal_velocity = 5.0
	def update(self, delta):
		self.velocity += gravity * delta
		if self.velocity.y > self.terminal_velocity:
			self.velocity.y = self.terminal_velocity
		self.velocity.add_to_rect(self.rect)
		sprites = pygame.sprite.spritecollide(self, self.level.platforms, dokill=False)
		if sprites:
			self.rect.y = sprites[0].rect.y - 40
	def is_updatable(self):
		return True
	def setup(self, level):
		self.level = level
		self.level.player = self
	def left_down(self):
		self.velocity += left
	def left_up(self):
		self.velocity += right
	def right_down(self):
		self.velocity += right
	def right_up(self):
		self.velocity += left
	def jump_start(self):
		self.velocity += up
	def jump_end(self):
		pass
