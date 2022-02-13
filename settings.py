import pygame
import sys
from pygame.locals import*

class Settings:

	def __init__(self):

		self.screen_width = 900
		self.screen_height = 900
		self.background_image = pygame.image.load('images/background.bmp')

		self.player_speed = 0.2

