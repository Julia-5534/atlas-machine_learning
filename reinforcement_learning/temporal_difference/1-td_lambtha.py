#!/usr/bin/env python3
"""Task 1"""

import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000,
               max_steps=100, alpha=0.1, gamma=0.99):
    """
    Performs the TD(λ) algorithm.

    Parameters:
    env: The OpenAI environment instance.
    V: A numpy.ndarray of shape (s,) containing the value estimate.
    policy: A function that takes in a state and returns the
    next action to take.
    lambtha: The eligibility trace factor.
    episodes: The total number of episodes to train over.
    max_steps: The maximum number of steps per episode.
    alpha: The learning rate.
    gamma: The discount rate.

    Returns:
    V: The updated value estimate.
    """
    for episode in range(episodes):
        state = env.reset()
        eligibility = np.zeros_like(V)
        for step in range(max_steps):
            action = policy(state)
            new_state, reward, done, _ = env.step(action)
            delta = reward + gamma * V[new_state] - V[state]
            eligibility[state] += 1.0
            V += alpha * delta * eligibility
            eligibility *= gamma * lambtha
            if done:
                break
            state = new_state

    return V
