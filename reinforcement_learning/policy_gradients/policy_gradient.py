#!/usr/bin/env python3
"""Tasks 0 & 1"""

import numpy as np


def policy(matrix, weight):
    """
    Computes the policy with a weight of a matrix.

    Parameters:
    matrix: A numpy array representing the state.
    weight: A numpy array representing the weight.

    Returns:
    policy: The computed policy.
    """
    z = matrix.dot(weight)
    exp = np.exp(z)
    return exp / np.sum(exp)


def policy_gradient(state, weight):
    """
    Computes the Monte-Carlo policy gradient based on
    a state and a weight matrix.

    Parameters:
    state: A numpy array representing the current observation
    of the environment.
    weight: A numpy array representing the weight.

    Returns:
    action: The chosen action.
    gradient: The computed gradient.
    """
    # Compute the probabilities for all actions
    probs = policy(state, weight).flatten()

    # Choose an action
    action = np.random.choice(len(probs), p=probs)

    # Compute the gradient
    d_logits = -probs
    d_logits[action] += 1
    gradient = state.T.dot(d_logits[None, :])

    return action, gradient
