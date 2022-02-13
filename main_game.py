import sys
import pygame
import math

from pygame.locals import *
from settings import Settings
from ninja import PlayerIdle
from npc import Npc




class Ninja:

	def __init__(self):

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Ninja")
		self.player = PlayerIdle(self)
		self.npc = Npc(self)
		

		

	def run_game(self):

		while True:
			self._check_events()
			self.player.update()
			self.npc.animate_idle()
			self._update_screen()



	def _update_screen(self):

		self.screen.blit(self.settings.background_image, (0, 0))
		self.npc.blitme()
		self.player.blitme()

		



		pygame.display.flip()

	def _check_events(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

		

	def _check_keydown_events(self, event):

		if event.key == pygame.K_RIGHT:
			self.player.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.player.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_UP:
			self.player.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.player.moving_down = True


	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.player.moving_right = False
			self.player.image = self.player.animations['idle'][1]
		elif event.key == pygame.K_LEFT:
			self.player.moving_left = False
			self.player.image = self.player.animations['idle'][0]
		elif event.key == pygame.K_UP:
			self.player.moving_up = False
			self.player.image = self.player.animations['idle'][2]
		elif event.key == pygame.K_DOWN:
			self.player.moving_down = False
			self.player.image = self.player.animations['idle'][2]

	

if __name__ == '__main__':

	ngame = Ninja()
	ngame.run_game()

