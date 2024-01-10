#!/usr/bin/env python3
"""Task 4"""

import numpy as np

def play(env, Q, max_steps=100):
    """
    Plays the Frozen Lake game using a trained model.

    Parameters:
    env: The Frozen Lake environment.
    Q: The Q-table.
    max_steps (int, optional): The maximum number of steps
    per game. Default is 100.

    Returns:
    total_rewards: The total reward for the game.
    """
    play_count = 5
    total_rewards = 0

    for episode in range(play_count):
        # Reset the environment to the starting state
        state = env.reset()

        for step in range(max_steps):
            # Choose the action with the highest expected reward
            action = np.argmax(Q[state, :])

            # Take the chosen action and observe the new state and reward
            new_state, reward, done, _ = env.step(action)[:4]

            # Update the total reward
            total_rewards += reward

            # Render the environment
            env.render()

            # Update the state
            state = new_state

            # End the game if the done flag is True
            if done:
                break

    return total_rewards
