import random

import pygame

class Apple(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.image = pygame.image.load('assets/objects/Apple Tile.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.game.screen.get_width() - self.image.get_width())
        self.rect.y = random.randint(0, self.game.screen.get_height() - self.image.get_height())

    def remove(self):
        self.game.all_apples.remove(self)