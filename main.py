import pygame
from game import Game

# set the FPS
clock = pygame.time.Clock()
FPS = 10

running = True

# load the game
game = Game()

while running:

    clock.tick(FPS)

    # update the screen
    pygame.display.flip()

    game.update()

    for event in pygame.event.get():

        # if the window is closing
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                game.pressed[event.key] = True

        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False

pygame.quit()



