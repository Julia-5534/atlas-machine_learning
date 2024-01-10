#!/usr/bin/env python3
"""Task 3"""

import numpy as np
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q,
          episodes=5000, max_steps=100,
          alpha=0.1, gamma=0.99,
          epsilon=1, min_epsilon=0.1,
          epsilon_decay=0.05):
    """
    Trains a model on the Frozen Lake environment using Q-learning.

    Parameters:
    env: The Frozen Lake environment.
    Q: The Q-table.
    episodes (int, optional): The number of episodes for
    training. Default is 5000.
    max_steps (int, optional): The maximum number of steps per
    episode. Default is 100.
    alpha (float, optional): The learning rate. Default is 0.1.
    gamma (float, optional): The discount factor. Default is 0.99.
    epsilon (float, optional): The initial exploration rate.
    Default is 1.
    min_epsilon (float, optional): The minimum exploration
    rate. Default is 0.1.
    epsilon_decay (float, optional): The decay rate for
    epsilon. Default is 0.05.

    Returns:
    Q: The updated Q-table after training.
    total_rewards: A list of the total rewards per episode.
    """

    total_rewards = []

    for episode in range(episodes):
        state = env.reset()
        episode_reward = 0

        for step in range(max_steps):
            action = epsilon_greedy(Q, state, epsilon)

            # Take the chosen action and observe the new state and reward
            step_result = env.step(action)
            new_state, reward, done, _ = step_result[:4]  # Take the first four values
            
            if reward == 1.0 and done is True:
                episode_reward += reward
            if reward == 0.0 and done is True:
                episode_reward -= 1
                reward = -1
            if reward == 0.0 and step + 1 == max_steps:
                episode_reward += 0

            # Update Q-value using the Q-learning update rule
            Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (
                reward + gamma * max(Q[new_state, :]))

            state = new_state
            episode_reward += reward

            if done:
                break

        # Decay epsilon
        epsilon = min_epsilon + (
            1 - min_epsilon) * np.exp(-epsilon_decay * episode)

        total_rewards.append(episode_reward)

    return Q, total_rewards
