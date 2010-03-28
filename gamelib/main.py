'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import data
import pygame
import sys
from constants import *

from engine import Engine

def main():
    game_data = {
        SIZE: (320, 240),
    }

    pygame.init()
    engine = Engine(game_data)
    engine.run()
