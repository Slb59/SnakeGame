import pygame
import time

class SoundManager:

    def __init__(self):
        self.sounds = {
            'gloup': pygame.mixer.Sound('assets/sound/plop.wav')
        }

    # use to play a sound
    def play(self, name):
        self.sounds[name].play()

    def play_ambiant(self):
        pygame.mixer.music.load('assets/sound/forest2.ogg')
        pygame.mixer.music.play(-1, 0.0)
        time.sleep(1)
