import pygame
from direction import Direction
from bodysnake import BodySnake


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

        self.velocity = 8
        self.length = 10

        self.all_body = pygame.sprite.Group()
        self.all_body.add(BodySnake(self))

    def check_wall_collision(self):
        collision = False
        if (self.direction == Direction.RIGHT and self.rect.x >= self.game.screen.get_width()) \
                or (self.direction == Direction.DOWN and self.rect.y >= self.game.screen.get_height()) \
                or (self.direction == Direction.LEFT and self.rect.x <= 0) \
                or (self.direction == Direction.UP and self.rect.y <= 0):
            collision = True

        return collision

    def move(self):

        print(self.rect.x)
        print(self.all_body.sprites()[len(self.all_body) - 1].rect.x)

        # add a body near the snake head
        if self.direction == Direction.RIGHT:
            if self.rect.x - self.all_body.sprites()[len(self.all_body) - 1].rect.x >= self.image.get_width() * 2:
                self.all_body.add(BodySnake(self))
        if self.direction == Direction.LEFT:
            if -(self.rect.x - self.all_body.sprites()[len(self.all_body) - 1].rect.x) >= self.image.get_width() * 2:
                self.all_body.add(BodySnake(self))
        if self.direction == Direction.UP:
            if -(self.rect.y - self.all_body.sprites()[len(self.all_body) - 1].rect.y) >= self.image.get_height() * 2:
                self.all_body.add(BodySnake(self))
        if self.direction == Direction.DOWN:
            if ((self.rect.y - self.all_body.sprites()[len(self.all_body) - 1].rect.y) >= self.image.get_height() * 2):
                self.all_body.add(BodySnake(self))

        # remove the last body
        if len(self.all_body) > self.length:
            self.all_body.remove(self.all_body.sprites()[0])

        if (self.check_wall_collision()) \
                or (self.game.check_collision(self, self.all_body)) \
                or (self.game.frame_iteration > 100 * self.length):
            self.rect.x = 0
            self.rect.y = 0
            self.game.game_over()
            self.game.add_score(-10)
            self.all_body = pygame.sprite.Group()
            self.all_body.add(BodySnake(self))
            self.game.reward = -10

        for apple in self.game.check_collision(self, self.game.all_apples):
            self.game.game_over()
            self.game.add_score(10)
            self.all_body.add(BodySnake(self))
            self.game.reward = 10

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
