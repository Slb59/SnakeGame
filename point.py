import pygame


class Point(pygame.sprite.Sprite):

    def __init__(self, snake, x, y):
        super().__init__()

        self.image = pygame.image.load('assets/objects/red-circle2.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,
                                            (snake.image.get_width(), snake.image.get_height()))
        self.rect.x = x
        self.rect.y = y
