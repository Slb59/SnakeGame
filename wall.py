import pygame

class Wall(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/objects/wall.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() / 4, self.image.get_height() / 4))
        self.rect.x = 0
        self.rect.y = 0
