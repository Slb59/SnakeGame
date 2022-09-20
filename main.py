import pygame
from game import Game
from agent import Agent
from helper import plot

running = True


plot_scores = []
plot_mean_scores = []
total_score = 0
record = 0

agent = Agent()
game = Game()

while running:

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

    print('Game', agent.n_games, 'Score', score, 'Record', record, 'done:', done)

    if done:
        # train the long memory, plot the result
        game.start()
        agent.n_games += 1
        agent.train_long_memory()

        if score > record:
            record = score
            agent.model.save()

        print('Game', agent.n_games, 'Score', score, 'Record', record)

        plot_scores.append(score)
        total_score += score
        mean_score = total_score / agent.n_games
        plot_mean_scores.append(mean_score)
        plot(plot_scores, plot_mean_scores)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



pygame.quit()



