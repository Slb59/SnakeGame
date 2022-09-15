from sound import SoundManager
from snake import Snake
import pygame

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

    def game_over(self):
        self.is_game_over = True

    def update(self):

        # setup player image
        self.screen.blit(self.snake.head_image, self.snake.head_image_rect)

        if self.is_game_over:
            self.snake.head_image_rect = (0, 0)
        else:
            self.snake.move()

        # change direction
        if self.pressed.get(pygame.K_RIGHT):
            self.snake.change_direction(1)
        elif self.pressed.get(pygame.K_LEFT):
            self.snake.change_direction(3)
        elif self.pressed.get(pygame.K_UP):
            self.snake.change_direction(4)
        elif self.pressed.get(pygame.K_DOWN):
            self.snake.change_direction(2)