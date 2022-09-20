import torch
import random
import numpy as np
from game import Game
from direction import Direction
from collections import deque
from collections import namedtuple

Point = namedtuple('Point', 'x, y')

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001


class Agent:

    def __init__(self):
        self.n_game = 0
        self.epsilon = 0
        self.gamma = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        # TODO : model, trainer

    def _is_collision(self, pos):
        return False

    def get_state(self, game):
        point_l = Point(game.snake.rect.x - game.snake.size, game.snake.rect.y)
        point_r = Point(game.snake.rect.x + game.snake.size, game.snake.rect.y)
        point_u = Point(game.snake.rect.x, game.snake.rect.y - game.snake.size)
        point_d = Point(game.snake.rect.x, game.snake.rect.y + game.snake.size)

        dir_l = game.snake.direction == Direction.LEFT
        dir_r = game.snake.direction == Direction.RIGHT
        dir_u = game.snake.direction == Direction.UP
        dir_d = game.snake.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and self.is_collision(point_r)) \
            or (dir_l and self.is_collision(point_l))



        ]

    def remember(self, state, action, reward, nex_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, nex_state, done):
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
            # get old state
            state_old = agent.get_state(game)
            # get move
            final_move = agent.get_action(state_old)
            # perform move and get new state
            reward, done, score = game.play_step(final_move)
            state_new = agent.get_state(game)

            # train the short memory
            agent.train_short_memory(state_old, final_move, reward, state_new, done)

            # remember
            agent.remember(state_old, final_move, reward, state_new, done)

            if done:
                # train the long memory, plot the result
                game.reset()
                agent.n_games += 1
                agent.train_long_memory()

                if score > record:
                    record = score
                    # agent.model.save()

                print('Game', agent.n_games, 'Score', score, 'Record', record)

                # TODO : plot

    if __name__ == '__main__':
        train()
