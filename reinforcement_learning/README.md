# Reinforcement Learning (RL)

Reinforcement Learning is a subset of machine learning where an agent learns to make decisions by interacting with its environment. The agent learns from the consequences of its actions, rather than from being explicitly taught and it selects its actions based on its past experiences (exploitation) and also by new choices (exploration).

## Topics in Reinforcement Learning

### 1. Q-Learning
Q-Learning is a value-based Reinforcement Learning algorithm that is used to determine the optimal action-selection policy using a q function. It enables an agent to learn how to act optimally in controlled Markovian domains. It defines a function Q: S x A -> R (Q from Quality), where S is the set of states and A is the set of actions. The agent interacts with the environment and updates the policy based on rewards returned by the environment.

### 2. Deep Q-Learning
Deep Q-Learning is a variant of Q-Learning that uses a deep neural network to approximate the Q-value function. The goal of Deep Q-Learning is to estimate the Q-values using Deep Learning techniques to solve complex Reinforcement Learning problems.

### 3. Policy Gradient Methods
Policy Gradient methods are a type of Reinforcement Learning algorithms that are well-suited for environments with high dimensional state and action spaces. Instead of learning a value function that tells us what is the expected sum of rewards given a state and an action, policy gradient methods directly learn the optimal policy.

### 4. Exploration vs Exploitation Trade-off
The exploration vs exploitation trade-off is a dilemma faced in Reinforcement Learning. Should the agent take the best action based on current knowledge (exploitation), or should the agent try a new action to see if it might be better (exploration)?

### 5. Temporal Difference Learning
Temporal Difference Learning is a combination of Monte Carlo ideas and dynamic programming (DP) ideas. Like Monte Carlo methods, Temporal Difference methods can learn directly from raw experience without a model of the environment's dynamics. Like DP, TD methods update estimates based on other learned estimates without waiting for a final outcome.

### 6. Multi-Armed Bandit Problems
The multi-armed bandit problem is a problem in which a fixed limited set of resources must be allocated between competing (alternative) choices in a way that maximizes their expected gain, when each choice's properties are only partially known at the time of allocation.

### 7. Bellman Equation
The Bellman equation, named after Richard E. Bellman, is a necessary condition for optimality associated with the mathematical optimization method known as dynamic programming. It writes the value of a decision problem at a certain point in time in terms of the payoff from some initial choices and the value of the remaining decision problem that results from those initial choices.

### 8. Markov Decision Process
A Markov Decision Process (MDP) is a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker. MDPs are useful for studying optimization problems solved via dynamic programming and reinforcement learning.
