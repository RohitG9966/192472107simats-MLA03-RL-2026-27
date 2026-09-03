import numpy as np

size = 5
V = np.zeros((size, size))

gamma = 0.9

goal = (4, 4)

for iteration in range(100):

    new_V = V.copy()

    for i in range(size):
        for j in range(size):

            if (i, j) == goal:
                new_V[i, j] = 10
                continue

            values = []

            if i > 0:
                values.append(-1 + gamma * V[i-1, j])

            if i < size - 1:
                values.append(-1 + gamma * V[i+1, j])

            if j > 0:
                values.append(-1 + gamma * V[i, j-1])

            if j < size - 1:
                values.append(-1 + gamma * V[i, j+1])

            new_V[i, j] = max(values)

    V = new_V

print("Optimal State-Value Function:")
print(np.round(V, 2))
