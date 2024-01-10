#!/usr/bin/env python3
"""Task 0"""

import gym
import gym.envs.toy_text


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """
    Loads the pre-made FrozenLakeEnv environment from OpenAI's gym.

    Parameters:
    desc (list of lists): A custom description of the map to
    load for the environment. Default is None.
    map_name (str): The pre-made map to load. Default is None.
    is_slippery (bool): A boolean to determine if the ice is
    slippery. Default is False.

    Returns:
    env: The FrozenLakeEnv environment.

    Note: If both desc and map_name are None, the environment will
    load a randomly generated 8x8 map.
    """

    # If both desc and map_name are None, generate a random 8x8 map
    if desc is None and map_name is None:
        desc = gym.envs.toy_text.frozen_lake.generate_random_map(size=8)

    # Load the FrozenLakeEnv environment with the given parameters
    env = gym.envs.toy_text.frozen_lake.FrozenLakeEnv(
        desc=desc, map_name=map_name, is_slippery=is_slippery)

    # Return the environment
    return env
