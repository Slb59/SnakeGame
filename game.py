from sound import SoundManager
from snake import Snake

class Game():
    def __init__(self):
        # manage sound
        self.sound_manager = SoundManager()
        self.sound_manager.play_ambiant()

        self.snake = Snake(self)

    def update(self, screen):

        # setup player image
        screen.blit(self.snake.head_image, self.snake.head_image_rect)