import numpy as np

temperatures = [18, 20, 22, 24, 26, 28]

actions = ["Cool", "Maintain", "Heat"]

weights = np.random.randn(3)

learning_rate = 0.01

for episode in range(100):

    temperature = np.random.choice(temperatures)

    total_reward = 0

    for step in range(20):

        probabilities = np.exp(weights) / np.sum(np.exp(weights))

        action = np.random.choice(3, p=probabilities)

        if temperature < 22 and action == 2:
            reward = 5
        elif temperature > 24 and action == 0:
            reward = 5
        elif 22 <= temperature <= 24 and action == 1:
            reward = 5
        else:
            reward = -2

        total_reward += reward

    weights += learning_rate * total_reward

print("REINFORCE training completed.")
print("Final weights:", weights)
