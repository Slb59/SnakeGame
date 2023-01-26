from utils.direction import Direction
from sound.sound import SoundManager
from snake import Snake
import pygame
from apple.apple import Apple
from wall.wall import Wall
import math

FPS = 80

class Game:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()

        self.SCREEN_WIDTH = 1080
        self.SCREEN_HEIGHT = 720

        # set the window game
        pygame.display.set_caption("Auto Snake Game")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.background = pygame.image.load('assets/ui/background 2.png')
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # manage sound
        self.sound_manager = SoundManager()
        self.sound_manager.play_ambiant()

        self.snake = Snake(self)

        self.is_game_over = False

        # the group of apples
        self.all_apples = pygame.sprite.Group()

        # the group of walls
        self.all_walls = pygame.sprite.Group()

        self.score = 0
        self.frame_iteration = 0
        self.reward = 0

        # tick between 2 game
        self.cooldown = 2000
        self.last_cooldown = pygame.time.get_ticks()

        self.draw_walls()
        self.start()

        self.clock = pygame.time.Clock()

    def draw_walls(self):
        wall = Wall()
        for i in range(math.ceil(self.SCREEN_WIDTH/wall.image.get_width())):
            wall = Wall()
            wall.rect.x += wall.image.get_width()*i
            wall.rect.y = - 5
            self.all_walls.add(wall)

            wall = Wall()
            wall.rect.x += wall.image.get_width()*i
            wall.rect.y = self.SCREEN_HEIGHT-10
            self.all_walls.add(wall)

        for i in range(math.ceil(self.SCREEN_HEIGHT/wall.image.get_height())):
            wall = Wall()
            wall.rect.x = - 5
            wall.rect.y += wall.image.get_height()*i
            self.all_walls.add(wall)

            wall = Wall()
            wall.rect.y += wall.image.get_height()*i
            wall.rect.x = self.SCREEN_WIDTH-10
            self.all_walls.add(wall)



    def start(self):

        self.snake.direction = Direction.RIGHT

        self.score = 0
        self.all_apples = pygame.sprite.Group()
        self.all_apples.add(Apple(self))
        self.is_game_over = False
        self.frame_iteration = 0

    def game_over(self):
        self.is_game_over = True

    def is_collision(self, sprite):
        if self.check_collision(sprite, self.all_walls) or self.check_collision(sprite, self.snake.all_body):
            return True
        else:
            return False

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def play_step(self, action):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # update frame iteration
        self.frame_iteration += 1

        self.snake.move(action)

        if (self.is_collision(self.snake)) or (self.frame_iteration > 100 * self.snake.length):
            self.snake.go_start()
            self.game_over()
            self.reward = -10
            self.snake.all_body = pygame.sprite.Group()
            self.snake.set_body()

        if self.check_collision(self.snake, self.all_apples):
            print('find the apple')
            self.game_over()
            self.snake.add_body()
            self.score += 1
            self.reward = 10

        self.update()
        self.clock.tick(FPS)

        return self.reward, self.is_game_over, self.score

    def update(self):

        # set background
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        # setup player image
        self.screen.blit(self.snake.image, self.snake.rect)

        # draw the apple
        self.all_apples.draw(self.screen)

        # draw the walls
        self.all_walls.draw(self.screen)

        # draw the body
        self.snake.all_body.draw(self.screen)

        # update the screen
        pygame.display.flip()


