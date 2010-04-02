import pygame
from game_object import GameObject
from util import Vector

gravity = Vector(x=0, y=1)
left = Vector(x=-2, y = 0)
right = Vector(x=2, y = 0)
up = Vector(x=0, y = -30)
down = Vector(x=0, y = 2)

class Player(GameObject):
	def __init__(self, x, y):
		super(Player, self).__init__(x*40, y*40, 40, 40)
		self.velocity = Vector()
		self.terminal_velocity = 10.0
		self.airborne = False
	def update(self, delta):
		self.velocity += gravity * delta
		if self.velocity.y > self.terminal_velocity:
			self.velocity.y = self.terminal_velocity
		self.velocity.add_to_rect(self.rect)
		self.airborne = True
		sprites = pygame.sprite.spritecollide(self, self.level.platforms, dokill=False)
		if sprites:
			sprite = sprites[0]
			self.rect.y = sprites[0].rect.y - 40
			self.airborne = False
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
		if not self.airborne:
			self.airborne = True
			self.velocity += up
	def jump_end(self):
		pass
