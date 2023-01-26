import torch
import random
import numpy as np
from utils.direction import Direction
from collections import deque
from app.point import Point
from model import Linear_QNet, QTrainer


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001


class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomless
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def get_state(self, game):

        point_l = Point(game.snake, game.snake.rect.x - game.snake.size, game.snake.rect.y)
        point_r = Point(game.snake, game.snake.rect.x + game.snake.size, game.snake.rect.y)
        point_u = Point(game.snake, game.snake.rect.x, game.snake.rect.y - game.snake.size)
        point_d = Point(game.snake, game.snake.rect.x, game.snake.rect.y + game.snake.size)

        dir_l = game.snake.direction == Direction.LEFT
        dir_r = game.snake.direction == Direction.RIGHT
        dir_u = game.snake.direction == Direction.UP
        dir_d = game.snake.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and game.is_collision(point_r)) \
            or (dir_l and game.is_collision(point_l)) \
            or (dir_u and game.is_collision(point_u)) \
            or (dir_d and game.is_collision(point_d)),

            # Danger right
            (dir_u and game.is_collision(point_r)) \
            or (dir_d and game.is_collision(point_l)) \
            or (dir_l and game.is_collision(point_u)) \
            or (dir_r and game.is_collision(point_d)),

            # Danger left
            (dir_d and game.is_collision(point_r)) \
            or (dir_u and game.is_collision(point_l)) \
            or (dir_r and game.is_collision(point_u)) \
            or (dir_l and game.is_collision(point_d)),

            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            # Food location
            game.all_apples.sprites()[0].rect.x < game.snake.rect.x,  # food left
            game.all_apples.sprites()[0].rect.x > game.snake.rect.x,  # food right
            game.all_apples.sprites()[0].rect.y < game.snake.rect.y,  # food up
            game.all_apples.sprites()[0].rect.y > game.snake.rect.y   # food down

        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, nex_state, done):
        self.memory.append((state, action, reward, nex_state, done))  #popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)  # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, nex_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, nex_states, dones)

    def train_short_memory(self, state, action, reward, nex_state, done):
        self.trainer.train_step(state, action, reward, nex_state, done)

    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        final_move = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:

            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move


