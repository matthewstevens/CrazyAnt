"""

"""
import pygame
from pygame.font import Font
from pygame.constants import MOUSEBUTTONUP, KEYDOWN, KEYUP
from constants import *

class MenuContext:
	def __init__(self, engine):
		self.engine = engine
		self.font = engine.game_data[FONT]
		self.start_text = self.font.render("Start", False, (255,255,255))
		self.start_text_rect = self.start_text.get_rect()
		self.start_text_rect.centerx = self.engine.screen.get_rect().centerx
		self.start_text_rect.centery = 20
		self.exit_text = self.font.render("Quit", False, (255,255,255))
		self.exit_text_rect = self.exit_text.get_rect()
		self.exit_text_rect.centerx = self.engine.screen.get_rect().centerx
		self.exit_text_rect.centery = 40
	def handle_mouse_up_event(self, event):
		if self.start_text_rect.collidepoint(event.pos):
			self.engine.context = GameContext(self.engine)
		elif self.exit_text_rect.collidepoint(event.pos):
			self.engine.running = False

	def handle_key_down_event(self, event):
		pass
	def handle_key_up_event(self, event):
		pass
	def display(self):
		self.engine.screen.blit(self.start_text, self.start_text_rect)
		self.engine.screen.blit(self.exit_text, self.exit_text_rect)

class GameContext:
	def __init__(self, engine):
		self.engine = engine
		self.font = engine.game_data[FONT]
	def handle_mouse_up_event(self, event):
		pass
	def handle_key_down_event(self, event):
		pass
	def handle_key_up_event(self, event):
		pass
	def display(self):
		pass

class Engine:
	def __init__(self, game_data):
		self.game_data = game_data
		self.screen = pygame.display.set_mode(game_data[SIZE])
		self.running = True
		self.context = MenuContext(self)

	def run(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					return
				if event.type == KEYDOWN:
					self.context.handle_key_down_event(event)
				elif event.type == KEYUP:
					self.context.handle_key_up_event(event)
				elif event.type == MOUSEBUTTONUP:
					self.context.handle_mouse_up_event(event)

			self.screen.fill((0,0,0))
			self.context.display()
			pygame.display.flip()
