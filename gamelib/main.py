'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import data
import pygame
from pygame.font import Font
import sys
from constants import *

from engine import Engine

def main():
	pygame.init()

	game_data = {
		SIZE: (640, 480),
		FONT: Font(None, 32),
		LEVELS: [
			"level1",
			"level2",
			"level3",
		],
		LEVEL_DATA: {
			"level1": {
				FILE: "level1.lvl",
			},
			"level2": {
				FILE: "level2.lvl",
			},
			"level3": {
				FILE: "level3.lvl",
			},
		}
	}

	engine = Engine(game_data)
	engine.run()
