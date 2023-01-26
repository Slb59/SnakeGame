import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/objects/wall2.png')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0
