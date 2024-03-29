# Q Learning Concepts

## 1. Markov Decision Process
A Markov Decision Process (MDP) is a mathematical framework used for modeling decision-making problems where the outcomes are partly random and partly controllable.

## 2. Environment
In AI, the environment refers to the surroundings or circumstances in which an AI system functions. It includes the physical environment, digital platforms, and virtualized worlds where AI models and algorithms are used.

## 3. Agent
In artificial intelligence, an agent is a computer program or system that is designed to perceive its environment, make decisions and take actions to achieve a specific goal or set of goals.

## 4. State
In AI, a state is a snapshot in time that represents some aspect of the problem.

## 5. Policy Function
A policy, denoted by μ, tells the agent what action to take at a particular state in the environment.

## 6. Value Function
A value function can be defined as the expected value of an agent in a certain state.

### 6.1 State-Value Function
The state-value function gives the expected return if we start from a state and act according to the policy.

### 6.2 Action-Value Function
The action-value function gives the expected return starting from a state, following a policy, and taking an action.

## 7. Discount Factor
The discount factor is a hyperparameter that determines the importance of future rewards. It is a value between 0 and 1, where 0 makes the agent "myopic" by only considering current rewards, and 1 makes it strive for a long-term high reward.

## 8. Bellman Equation
The Bellman equation is a necessary condition for optimality associated with the mathematical optimization method known as dynamic programming.

## 9. Epsilon Greedy
Epsilon Greedy is a strategy for balancing exploration and exploitation in reinforcement learning. The agent chooses the best action most of the time, but with a probability of epsilon, it will explore the environment by choosing any action randomly.

## 10. Q-Learning
Q-Learning is a values based algorithm in reinforcement learning. It's used to find the optimal action-selection policy using a q function. It evaluates which action to take based on an action-value function that determines the value of being in a certain state and taking a certain action at that state.

# Q Learning Project
