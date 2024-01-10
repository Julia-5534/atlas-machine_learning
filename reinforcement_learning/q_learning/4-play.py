#!/usr/bin/env python3
"""Task 4"""

import numpy as np


def play(env, Q, max_steps=100):
    """Plays Frozen Lake"""
    state = env.reset()
    total_rewards = 0

    for step in range(max_steps):
        action = np.argmax(Q[state, :])
        new_state, reward, done, _ = (env.step(action)[:4])
        total_rewards += reward
        env.render()
        state = new_state
        total_rewards += reward
        if done:
            break
    return total_rewards
