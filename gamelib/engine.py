"""

"""
import pygame
from constants import *

class Engine:
    def __init__(self, game_data):
        self.game_data = game_data
        self.screen = pygame.display.set_mode(game_data[SIZE])
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    continue

            self.screen.fill((0,0,0))
            pygame.display.flip()
