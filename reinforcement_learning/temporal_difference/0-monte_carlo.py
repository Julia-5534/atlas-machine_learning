#!/usr/bin/env python3
"""Task 0"""

import numpy as np


def monte_carlo(env, V, policy, episodes=5000,
                max_steps=100, alpha=0.1, gamma=0.99):
    """
    Performs the Monte Carlo algorithm.

    Parameters:
    env: The OpenAI environment instance.
    V: A numpy.ndarray of shape (s,) containing the value estimate.
    policy: A function that takes in a state and returns the next
    action to take.
    episodes: The total number of episodes to train over.
    max_steps: The maximum number of steps per episode.
    alpha: The learning rate.
    gamma: The discount rate.

    Returns:
    V: The updated value estimate.
    """
    for episode in range(episodes):
        state = env.reset()
        done = False
        steps = []
        for step in range(max_steps):
            action = policy(state)
            new_state, reward, done, _ = env.step(action)
            steps.append((state, action, reward))
            if done:
                break
            state = new_state

        G = 0
        for i, step in enumerate(reversed(steps)):
            state, action, reward = step
            G = gamma * G + reward
            if state not in [x[0] for x in steps[::-1][i+1:]]:
                V[state] = V[state] + alpha * (G - V[state])

    # Set print options for NumPy to format the output as desired
    np.set_printoptions(precision=4, suppress=True)

    return V
