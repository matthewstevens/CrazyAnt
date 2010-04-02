"""
Helpful stuff that is useful for everyone
"""

import os
from pygame import Rect

FILE_PATH = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = os.path.normpath(os.path.join(FILE_PATH, '..', 'data'))

def file_path(file_name):
	return os.path.join(DATA_PATH, file_name)

def load(file_name):
	return open(file_path(file_name))

def relative_rect(obj, camera):
    return Rect(obj.x - camera.x, obj.y - camera.y, obj.width, obj.height)
