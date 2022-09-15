import pygame

pygame.init()
pygame.mixer.init()

# set the FPS
clock = pygame.time.Clock()
FPS = 100

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# set the window game
pygame.display.set_caption("Auto Snake Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('assets/ui/background 2.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:

    clock.tick(FPS)

    # update the screen
    pygame.display.flip()

    # set background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        # if the window is closing
        if event.type == pygame.QUIT:
            pygame.quit()



