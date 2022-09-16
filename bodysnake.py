import  pygame
from direction import Direction

class BodySnake(pygame.sprite.Sprite):

    def __init__(self, snake):
        super().__init__()

        # load the body image
        self.image = pygame.image.load('assets/objects/snake body.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() / 4, self.image.get_height() / 4))

        self.snake = snake

        if self.snake.direction == Direction.RIGHT:
            self.rect.x = self.snake.rect.x - self.snake.image.get_width()
            self.rect.y = self.snake.rect.y
        if self.snake.direction == Direction.LEFT:
            self.rect.x = self.snake.rect.x + self.snake.image.get_width()
            self.rect.y = self.snake.rect.y
        if self.snake.direction == Direction.UP:
            self.rect.x = self.snake.rect.x
            self.rect.y = self.snake.rect.y + self.snake.image.get_height()
        if self.snake.direction == Direction.DOWN:
            self.rect.x = self.snake.rect.x
            self.rect.y = self.snake.rect.y - self.snake.image.get_height()


