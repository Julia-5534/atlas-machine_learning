# Deep Q-Learning Concepts

## 1. Deep Q-Learning
Deep Q-Learning is a reinforcement learning algorithm that combines Q-Learning, an algorithm for learning optimal actions in an environment, with deep neural networks. It enables an agent to learn how to make optimal decisions in an environment by maximizing cumulative rewards.

## 2. Policy Network
In the context of reinforcement learning, a policy network is a neural network that maps game states to a distribution of the likelihood of taking each action. This distribution covers all possible actions from that state.

## 3. Replay Memory
Replay memory is a machine learning technique that stores and reuses past experiences to enhance an agent's decision-making. Common in reinforcement learning, it helps agents learn from diverse situations, improving performance in applications like game AI, robotics, and autonomous vehicles.

## 4. Target Network
In Deep Q-Learning, a target network is used, which is a copy of the main network but updated less frequently. This helps keep runaway bias from bootstrapping from dominating the system numerically, causing the estimated Q values to diverge.

## 5. Why Utilize Two Separate Networks During Training
The use of two separate networks during training in AI, such as in Deep Q-Learning, is to do with the stability of the Q-learning algorithm when using function approximation (i.e., the neural network). Using a separate target network, updated every so many steps with a copy of the latest learned parameters, helps keep runaway bias from bootstrapping from dominating the system numerically, causing the estimated Q values to diverge.

## 6. Keras-RL
Keras-RL is a Python library that implements some state-of-the-art deep reinforcement learning algorithms. It seamlessly integrates with the deep learning library Keras and works with OpenAI Gym out of the box. Keras-RL provides a range of pre-trained models that can be used as starting points for training new models.

# Deep Q-Learning Project
