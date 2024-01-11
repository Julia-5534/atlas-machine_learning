#!/usr/bin/env python3
"""Play"""

import gym
from keras.models import Sequential
from keras.layers import Dense, Flatten
from rl.agents import DQNAgent
from rl.policy import GreedyQPolicy


# Create the Breakout environment
env = gym.make('Breakout-v4')

# Define the number of actions and the input shape
nb_actions = env.action_space.n
input_shape = env.observation_space.shape

# Create the neural network model
model = Sequential()
model.add(Flatten(input_shape=input_shape))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(nb_actions, activation='linear'))

# Create the DQN agent
dqn = DQNAgent(model=model, nb_actions=nb_actions, policy=GreedyQPolicy())

# Load the policy network
dqn.load_weights('policy.h5')

# Play the game
dqn.test(env, nb_episodes=1, visualize=True)
