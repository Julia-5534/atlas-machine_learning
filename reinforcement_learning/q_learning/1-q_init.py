#!/usr/bin/env python3
"""Task 1"""

import numpy as np


def q_init(env):
    """
    This function initializes the Q-table for the FrozenLake environment.

    Parameters:
    env (FrozenLakeEnv instance): The FrozenLake environment.

    Returns:
    Q (numpy.ndarray): The Q-table as a numpy.ndarray of zeros.
    """

    # Get the number of states and actions from the environment
    num_states = env.observation_space.n
    num_actions = env.action_space.n

    # Initialize the Q-table with zeros
    Q = np.zeros((num_states, num_actions))

    # Return the Q-table
    return Q
