#!/usr/bin/env python3
"""Training Model for Atari's Breakout"""

import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from gym.wrappers import RecordEpisodeStatistics, RecordVideo
from rl.agents import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory


# Environment setup
env = gym.make('Breakout-v4')
env = RecordVideo(env, './deepqbreakout.mp4', episode_trigger=lambda episode: True)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n

# Build a simple model
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))

# Configure and compile our agent
memory = SequentialMemory(limit=50000, window_length=1)
policy = EpsGreedyQPolicy(0.3)
agent = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10000,
               target_model_update=1e-2, policy=policy)
agent.compile(Adam(lr=1e-3), metrics=['mae'])

# Train the agent
agent.fit(env, nb_steps=50000, visualize=False, verbose=2)

# Save the final policy network
agent.save_weights('./policy.h5', overwrite=True)
