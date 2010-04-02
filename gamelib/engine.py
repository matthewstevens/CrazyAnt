"""

"""
import pygame
from pygame.font import Font
from pygame.constants import MOUSEBUTTONUP, KEYDOWN, KEYUP, K_ESCAPE, K_a, K_d
from constants import *
from level import Level
from util import load

class MenuContext:
	def __init__(self, engine):
		self.engine = engine
		offset = 20
		self.font = engine.game_data[FONT]
		self.start_text = self.font.render("Start", False, (255,255,255))
		self.start_text_rect = self.start_text.get_rect()
		self.start_text_rect.centerx = self.engine.screen.get_rect().centerx
		self.start_text_rect.centery = offset
		offset += 20
		self.continue_text_rect = None
		if self.engine.current_game_context:
			self.continue_text = self.font.render("Continue", False, (255,255,255))
			self.continue_text_rect = self.continue_text.get_rect()
			self.continue_text_rect.centerx = self.engine.screen.get_rect().centerx
			self.continue_text_rect.centery = offset
			offset += 20
		self.exit_text = self.font.render("Quit", False, (255,255,255))
		self.exit_text_rect = self.exit_text.get_rect()
		self.exit_text_rect.centerx = self.engine.screen.get_rect().centerx
		self.exit_text_rect.centery = offset
		print "Menu Created"
	def handle_mouse_up_event(self, event):
		if self.continue_text_rect and self.continue_text_rect.collidepoint(event.pos):
			self.engine.context = self.engine.current_game_context
		if self.start_text_rect.collidepoint(event.pos):
			new_game = GameContext(self.engine)
			self.engine.context = new_game
			self.engine.current_game_context = new_game
		elif self.exit_text_rect.collidepoint(event.pos):
			self.engine.running = False

	def handle_key_down_event(self, event):
		pass
	def handle_key_up_event(self, event):
		if event.key == K_ESCAPE:
			self.engine.running = False
	def update(self, delta):
		pass
	def display(self):
		self.engine.screen.blit(self.start_text, self.start_text_rect)
		self.engine.screen.blit(self.exit_text, self.exit_text_rect)
		if self.continue_text_rect:
			self.engine.screen.blit(self.continue_text, self.continue_text_rect)

class GameContext:
	def __init__(self, engine):
		self.engine = engine
		self.font = engine.game_data[FONT]
		self.current_level = 0
		self.current_level_id = self.engine.game_data[LEVELS][self.current_level]
		self.level = Level(load(self.engine.game_data[LEVEL_DATA][self.current_level_id][FILE]), engine)
		controls = engine.game_data[CONTROLS]
		self.down_control_map = {
			controls[LEFT]: self.level.player.left_down,
			controls[RIGHT]: self.level.player.right_down,
			controls[JUMP]: self.level.player.jump_start,
		}
		self.up_control_map = {
			controls[LEFT]: self.level.player.left_up,
			controls[RIGHT]: self.level.player.right_up,
			controls[JUMP]: self.level.player.jump_end,
		}
		print "Game Created"
	def handle_mouse_up_event(self, event):
		pass
	def handle_key_down_event(self, event):
		if self.down_control_map.has_key(event.key):
			self.down_control_map[event.key]()
	def handle_key_up_event(self, event):
		if event.key == K_ESCAPE:
			self.engine.context = MenuContext(self.engine)
		elif self.down_control_map.has_key(event.key):
			self.up_control_map[event.key]()
	def update(self, delta):
		self.level.update(delta)
	def display(self):
		self.level.draw(self.engine.screen)

class Engine:
	def __init__(self, game_data):
		self.game_data = game_data
		self.screen = pygame.display.set_mode(game_data[SIZE])
		pygame.display.set_caption(game_data[TITLE])
		self.running = True
		self.current_game_context = None
		self.context = MenuContext(self)
		self.clock = pygame.time.Clock()

	def run(self):
		#old_time = pygame.time.get_ticks()
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
			delta = self.clock.tick(60) / 1000.0
			#now = pygame.time.get_ticks()
			#print (now - old_time)
			#delta = (now - old_time) / 1000.0
			#old_time = now
			#delta = 0.011
			self.context.update(delta)
			self.screen.fill((0,0,0))
			self.context.display()
			pygame.display.flip()
