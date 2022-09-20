from direction import Direction
from sound import SoundManager
from snake import Snake
import pygame
from apple import Apple
from wall import Wall
from point import Point


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


        # manage pressed key
        self.pressed = {}

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

    def draw_walls(self):
        for i in range(self.SCREEN_WIDTH):
            wall = Wall()
            wall.rect.x += wall.image.get_width()*i
            wall.rect.y = - 20
            self.all_walls.add(wall)

            wall = Wall()
            wall.rect.x += wall.image.get_width()*i
            wall.rect.y = self.SCREEN_HEIGHT-10
            self.all_walls.add(wall)

        for i in range(self.SCREEN_HEIGHT):
            wall = Wall()
            wall.rect.x = - 20
            wall.rect.y += wall.image.get_height()*i
            self.all_walls.add(wall)

            wall = Wall()
            wall.rect.y += wall.image.get_height()*i
            wall.rect.x = self.SCREEN_WIDTH-10
            self.all_walls.add(wall)

    def add_score(self, amount):
        self.score += amount
    def start(self):

        self.all_apples.add(Apple(self))
        self.is_game_over = False
        self.snake.direction = Direction.RIGHT

    def game_over(self):
        self.all_apples = pygame.sprite.Group()
        self.is_game_over = True
        self.last_cooldown = pygame.time.get_ticks()
        self.frame_iteration = 0

    def is_collision(self, sprite):
        return self.check_collision(sprite, self.all_walls) \
            or self.check_collision(sprite, self.snake.all_body)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

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

        # update frame iteration
        self.frame_iteration += 1

        if self.is_game_over:

            time_now = pygame.time.get_ticks()

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
