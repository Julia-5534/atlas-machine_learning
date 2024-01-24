#!/usr/bin/env python3
"""Tasks 2 & 3"""

import numpy as np
import matplotlib.pyplot as plt
policy_gradient = __import__('policy_gradient').policy_gradient


def train(env, nb_episodes, alpha=0.000045, gamma=0.98, show_result=False):
    """
    Implements a full training.

    Parameters:
    env: The initial environment.
    nb_episodes: The number of episodes used for training.
    alpha: The learning rate.
    gamma: The discount factor.
    show_result: Whether to render the environment every 1000 episodes.

    Returns:
    scores: All values of the score (sum of all rewards during
    one episode loop).
    """
    # Initialize the weight
    weight = np.random.rand(*env.observation_space.shape, env.action_space.n)

    # Initialize the scores
    scores = []

    for episode in range(1, nb_episodes + 1):
        state = env.reset()[None, :]
        grad = 0
        score = 0
        done = False

        while not done:
            # Compute the action and the gradient
            action, delta_grad = policy_gradient(state, weight)

            # Take a step in the environment
            new_state, reward, done, info = env.step(action)
            new_state = new_state[None, :]

            # Update the score
            score += reward

            # Compute the gradient
            grad += delta_grad

            # Update the weight
            weight += alpha * grad * (
                reward + gamma * np.max(new_state.dot(
                    weight)) * (not done) - state.dot(
                        weight)[0, action])

            # Update the state
            state = new_state

        # Store the score
        scores.append(score)

        # Print the current episode number and the score
        print("Episode: {}, Score: {}".format(
            episode, score), end="\r", flush=False)

        # Render the environment every 1000 episodes
        if show_result and episode % 1000 == 0:
            env.render()

    return scores
