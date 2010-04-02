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

class Vector(object):
	def __init__(self, vector = None, x = 0.0, y = 0.0):
		if vector:
			self.x = vector.x
			self.y = vector.y
		else:
			self.x = x
			self.y = y
	def add_to_rect(self, rect):
		rect.x += self.x
		rect.y += self.y
	def __mul__(self, other):
		v = Vector(vector=self)
		if type(other) == 'float':
			v.x *= other
			v.y *= other
		return v
	def __iadd__(self, other):
		if other.__class__.__name__ == 'Vector':
			self.x += other.x
			self.y += other.y
		else:
			self.x += other
			self.y += other
		return self
	def len_sqrd(self):
		return (self.x * self.x) + (self.y * self.y)
