from direction import Direction
from sound import SoundManager
from snake import Snake
import pygame
from apple import Apple

class Game():
    def __init__(self, screen):

        self.screen = screen

        # manage sound
        self.sound_manager = SoundManager()
        self.sound_manager.play_ambiant()

        self.snake = Snake(self)

        # manage pressed key
        self.pressed = {}

        self.is_game_over = False

        # the group off apples
        self.all_apples = pygame.sprite.Group()

        self.score = 0

        # tick between 2 game
        self.cooldown = 2000
        self.last_cooldown = pygame.time.get_ticks()

        self.start()
    def add_score(self, amount):
        self.score += amount
    def start(self):
        self.all_apples.add(Apple(self))
        self.is_game_over = False

    def game_over(self):
        self.all_apples = pygame.sprite.Group()
        self.is_game_over = True
        self.last_cooldown = pygame.time.get_ticks()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self):

        # setup player image
        self.screen.blit(self.snake.image, self.snake.rect)

        # draw the apple
        self.all_apples.draw(self.screen)

        if self.is_game_over:

            self.snake.rect.x = 0
            self.snake.rect.y = 0
            self.snake.direction = Direction.RIGHT

            time_now = pygame.time.get_ticks()
            print(time_now - self.last_cooldown)
            if time_now - self.last_cooldown > self.cooldown:
                self.start()
                self.last_cooldown = pygame.time.get_ticks()

        else:
            self.snake.move()

        # change direction
        if self.pressed.get(pygame.K_RIGHT):
            self.snake.change_direction(Direction.RIGHT)
        elif self.pressed.get(pygame.K_LEFT):
            self.snake.change_direction(Direction.LEFT)
        elif self.pressed.get(pygame.K_UP):
            self.snake.change_direction(Direction.UP)
        elif self.pressed.get(pygame.K_DOWN):
            self.snake.change_direction(Direction.DOWN)
