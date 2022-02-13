from pygame_functions import *

class Sprites:

	def __init__(self):

		self.sprite = makeSprite("animacje/ninjaup.gif", 4)
		self.nextFrame = clock()
		self.frame = 0

	def add_frame(self):

		while True:
			if clock() > self.nextFrame:
				self.frame = (self.frame+1)%4
				self.nextFrame += 180

			if keyPressed("up"):
				changeSpriteImage(self.Sprite, 0*4 + self.frame)


