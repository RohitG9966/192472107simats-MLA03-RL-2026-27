import numpy as np

# Simple lane-keeping environment
class LaneKeepingEnv:
    def __init__(self):
        self.state = 0.0
        self.target = 0.0

    def reset(self):
        self.state = np.random.uniform(-1, 1)
        return self.state

    def step(self, action):
        self.state += action
        error = abs(self.target - self.state)

        if error < 0.1:
            reward = 10
        else:
            reward = -error

        done = error < 0.1 or abs(self.state) > 2
        return self.state, reward, done


# Policy Gradient Agent
class PolicyGradientAgent:
    def __init__(self, learning_rate=0.01):
        self.weights = np.random.randn(2)
        self.lr = learning_rate

    def policy(self, state):
        x = np.array([state, 1])
        probability = 1 / (1 + np.exp(-np.dot(self.weights, x)))
        return probability

    def choose_action(self, state):
        p = self.policy(state)

        if np.random.rand() < p:
            return -0.1
        else:
            return 0.1

    def update(self, states, actions, rewards):
        G = 0

        for state, action, reward in reversed(
                list(zip(states, actions, rewards))):

            G += reward

            x = np.array([state, 1])
            p = self.policy(state)

            if action == -0.1:
                gradient = (1 - p) * x
            else:
                gradient = -p * x

            self.weights += self.lr * G * gradient


# Training
env = LaneKeepingEnv()
agent = PolicyGradientAgent()

episodes = 100

for episode in range(episodes):

    state = env.reset()

    states = []
    actions = []
    rewards = []

    done = False

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        states.append(state)
        actions.append(action)
        rewards.append(reward)

        state = next_state

    agent.update(states, actions, rewards)

    if episode % 10 == 0:
        print("Episode:", episode,
              "Total Reward:", round(sum(rewards), 2))

print("\nTraining completed.")
print("Final Policy Weights:", agent.weights)
