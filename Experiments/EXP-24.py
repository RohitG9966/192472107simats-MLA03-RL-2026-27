import numpy as np

prices = [100, 102, 101, 105, 107, 106, 110, 112]

actions = ["Buy", "Sell", "Hold"]

weights = np.random.randn(3)

learning_rate = 0.01

for episode in range(100):

    total_reward = 0
    states = []
    selected_actions = []
    rewards = []

    for i in range(len(prices) - 1):

        state = prices[i]

        probabilities = np.exp(weights) / np.sum(np.exp(weights))

        action = np.random.choice(3, p=probabilities)

        if action == 0:
            reward = prices[i + 1] - prices[i]
        elif action == 1:
            reward = prices[i] - prices[i + 1]
        else:
            reward = 0

        states.append(state)
        selected_actions.append(action)
        rewards.append(reward)

        total_reward += reward

    G = 0

    for reward in reversed(rewards):
        G += reward
        weights += learning_rate * G

print("Training completed.")
print("Final policy weights:")
print(weights)

print("Total reward:", round(total_reward, 2))
