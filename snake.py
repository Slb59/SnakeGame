import pygame
from direction import Direction
from bodysnake import BodySnake
import numpy as np

class Snake(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        # load the head image
        self.image = pygame.image.load('assets/objects/snake head.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() / 4, self.image.get_height() / 4))

        # direction of the snake
        self.direction = Direction.RIGHT

        self.velocity = self.image.get_width()
        self.length = 10

        self.all_body = pygame.sprite.Group()
        self.set_body()

    def set_body(self):
        for i in range(self.length):
            new_body = BodySnake(self)
            new_body.set_position(self.rect.x - self.image.get_width()*i, self.rect.y)
            self.all_body.add(new_body)

    def check_wall_collision(self):
        collision = False
        if (self.direction == Direction.RIGHT and self.rect.x >= self.game.screen.get_width()) \
                or (self.direction == Direction.DOWN and self.rect.y >= self.game.screen.get_height()) \
                or (self.direction == Direction.LEFT and self.rect.x <= 0) \
                or (self.direction == Direction.UP and self.rect.y <= 0):
            collision = True

        return collision

    def move(self, action=[1, 0, 0]):

        if (self.check_wall_collision()) \
                or (self.game.frame_iteration > 100 * self.length):
            self.rect.x = 0
            self.rect.y = 0
            self.game.game_over()
            self.game.add_score(-10)
            self.all_body = pygame.sprite.Group()
            self.set_body()
            self.game.reward = -10

        for apple in self.game.check_collision(self, self.game.all_apples):
            self.game.game_over()
            self.game.add_score(10)
            self.all_body.add(BodySnake(self))
            self.length += 1
            self.game.reward = 10

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]  # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]  # right turn
        else:
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]  # left turn

        self.direction = new_dir

        # move the body
        i = len(self.all_body) - 1
        while i > 0:
            self.all_body.sprites()[i].rect.x = self.all_body.sprites()[i-1].rect.x
            self.all_body.sprites()[i].rect.y = self.all_body.sprites()[i - 1].rect.y
            i = i-1
        self.all_body.sprites()[0].rect.x = self.rect.x
        self.all_body.sprites()[0].rect.y = self.rect.y

        # move he head
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
