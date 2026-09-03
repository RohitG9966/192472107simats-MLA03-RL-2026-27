import numpy as np

size = 5

Q = np.zeros((size, size, 4))

actions = ["Up", "Down", "Left", "Right"]

alpha = 0.1
gamma = 0.9

for episode in range(500):

    x, y = 0, 0

    for step in range(50):

        action = np.random.randint(4)

        nx, ny = x, y

        if action == 0:
            nx = max(0, x - 1)
        elif action == 1:
            nx = min(size - 1, x + 1)
        elif action == 2:
            ny = max(0, y - 1)
        else:
            ny = min(size - 1, y + 1)

        if (nx, ny) == (4, 4):
            reward = 10
        else:
            reward = -1

        Q[x, y, action] += alpha * (
            reward +
            gamma * np.max(Q[nx, ny]) -
            Q[x, y, action]
        )

        x, y = nx, ny

        if (x, y) == (4, 4):
            break

print("Training completed.")

print("\nLearned Q-values:")
print(Q)
