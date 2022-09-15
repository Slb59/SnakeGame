import pygame

class Snake(pygame.sprite.Sprite):

    def __init__(self, game):

        self.game = game

        # load the head image
        self.head_image = pygame.image.load('assets/objects/snake head.png')
        self.head_image_rect = self.head_image.get_rect()
        self.head_image = pygame.transform.scale(self.head_image,
                                                 (self.head_image.get_width() / 4, self.head_image.get_height() / 4))

        # load the body image
        self.body_image = pygame.image.load('assets/objects/snake body.png')
        self.body_image_rect = self.body_image.get_rect()

        self.all_body = pygame.sprite.Group()

    def move_right(self):
        self.head_image_rect.x += 1

    def move_left(self):
        self.head_image_rect.x += 1

    def move_up(self):
        self.head_image_rect.y -= 1

    def move_down(self):
        self.head_image_rect.y += 1
