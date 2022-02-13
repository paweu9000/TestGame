import pygame
from support import import_folder


class PlayerIdle:

	def __init__(self, ngame_game):


		self.screen = ngame_game.screen
		self.settings = ngame_game.settings
		self.screen_rect = ngame_game.screen.get_rect()

		self.frame_index = 0
		self.animation_speed = 0.005
		self.import_character_sprites()
		self.image = self.animations['idle'][2]
		self.rect = self.image.get_rect()
		
		self.rect.midbottom = self.screen_rect.midbottom

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.velocity_x = 0
		self.rect.height = 64
		self.rect.width = 64
		self.running = False

	def blitme(self):
		
		self.screen.blit(self.image, self.rect)

	def update(self):

		if self.moving_right and self.rect.right < 900:
			self.x += self.settings.player_speed
			self.animate_right()
			self.velocity_x = 1
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.player_speed
			self.animate_left()
			self.velocity_x = -1
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.player_speed
			self.animate_up()
		if self.moving_down and self.rect.bottom < 900:
			self.y += self.settings.player_speed
			self.animate_down()

		self.rect.x = self.x
		self.rect.y = self.y

	def import_character_sprites(self):

		character_path = 'animations/'
		self.animations = {'idle':[], 'runup':[], 'runleft':[], 'runright':[], 'rundown':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def animate_up(self):

		animation = self.animations['runup']
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]

	def animate_left(self):

		animation = self.animations['runleft']
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]

	def animate_right(self):

		animation = self.animations['runright']
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]

	def animate_down(self):

		animation = self.animations['rundown']
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]

	


	
	

