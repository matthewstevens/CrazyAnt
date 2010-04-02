'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import os
import data
import pygame
from constants import *
from pygame.font import Font
import sys
from pygame.constants import K_a, K_d, K_s

from engine import Engine

def main():
	os.environ["SDL_VIDEO_CENTERED"] = "1"
	pygame.init()

	game_data = {
		TITLE: "Crazy Ant",
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
		},
		CONTROLS: {
			LEFT: K_a,
			RIGHT: K_d,
			JUMP: K_s
		},
	}

	engine = Engine(game_data)
	engine.run()
