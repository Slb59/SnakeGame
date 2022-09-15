import pygame
from sound import SoundManager

class Game():
    def __init__(self):
        # manage sound
        self.sound_manager = SoundManager()
        self.sound_manager.play_ambiant()

    def update(self, screen):
        pass