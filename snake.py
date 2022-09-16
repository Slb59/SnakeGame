import pygame
from direction import Direction

class Snake(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        # load the head image
        self.image = pygame.image.load('assets/objects/snake head.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,
                                                 (self.image.get_width() / 4, self.image.get_height() / 4))

        # load the body image
        self.body_image = pygame.image.load('assets/objects/snake body.png')
        self.body_image_rect = self.body_image.get_rect()

        self.all_body = pygame.sprite.Group()

        # direction of the snake
        self.direction = Direction.RIGHT

        self.velocity = 5

    def check_wall_collision(self):
        collision = False
        if (self.direction == Direction.RIGHT and self.rect.x >= self.game.screen.get_width()) \
                or (self.direction == Direction.DOWN and self.rect.y >= self.game.screen.get_height())\
                or (self.direction == Direction.LEFT and self.rect.x <= 0)\
                or (self.direction == Direction.UP and self.rect.y <= 0):
            collision = True

        return collision
    def move(self):
        if self.check_wall_collision():
            self.game.game_over()
            self.game.add_score(-10)

        for apple in self.game.check_collision(self, self.game.all_apples):
            self.game.game_over()
            self.game.add_score(10)

        if self.direction == Direction.RIGHT:
            self.rect.x += self.velocity
        if self.direction == Direction.DOWN:
            self.rect.y += self.velocity
        if self.direction == Direction.LEFT:
            self.rect.x -= self.velocity
        if self.direction == Direction.UP:
            self.rect.y -= self.velocity
    def change_direction(self, value):
        self.direction = value



