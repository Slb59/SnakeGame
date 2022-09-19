import torch
import random
import numpy as np
from game import Game
from direction import Direction
from collections import deque

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_game = 0
        self.epsilon = 0
        self.gamma = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        #TODO : model, trainer

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, nex_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self):
        pass

    def get_action(self, state):
        pass

    def train(self):
        plot_scores = []
        plot_mean_scores = []
        total_score = 0
        record = 0
        agent = Agent()
        game = Game()
        while True:
            state_old = agent.get_state(game)
            final_move = agent.get_action(state_old)


    if __name__ == '__main__':
        train()
