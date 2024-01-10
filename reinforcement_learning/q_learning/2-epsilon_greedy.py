#!/usr/bin/env python3
"""Task 2"""

import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    This function uses epsilon-greedy to determine the next action.

    Parameters:
    Q (numpy.ndarray): The Q-table.
    state (int): The current state.
    epsilon (float): The epsilon to use for the calculation.

    Returns:
    action (int): The next action index.
    """

    # Sample p with numpy.random.uniform to determine if
    # the algorithm should explore or exploit
    p = np.random.uniform(0, 1)

    # If p is less than epsilon, the algorithm should explore
    if p < epsilon:
        # Pick the next action with numpy.random.randint
        # from all possible actions
        action = np.random.randint(Q.shape[1])
    else:
        # Otherwise, the algorithm should exploit
        # Pick the action with the highest Q-value for the current state
        action = np.argmax(Q[state, :])

    # Return the next action index
    return action
