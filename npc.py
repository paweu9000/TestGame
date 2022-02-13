import pygame
from support import import_folder


class Npc:

	def __init__(self, ngame_game):

		self.screen = ngame_game.screen
		self.settings = ngame_game.settings
		self.screen_rect = ngame_game.screen.get_rect()

		self.import_npc_sprites()
		self.image = self.animations['testnpcidle'][1]
		self.rect = self.image.get_rect(center =(450, 450))

		self.frame_index = 0
		self.animation_speed = 0.015

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.height = 64
		self.width = 64

	def blitme(self):

		self.screen.blit(self.image, self.rect)

	def import_npc_sprites(self):

		character_path = 'animations/'
		self.animations = {'testnpcidle':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def animate_idle(self):

		animation = self.animations['testnpcidle']
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]

	