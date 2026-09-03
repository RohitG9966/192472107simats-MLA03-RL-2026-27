import numpy as np

tasks = {
    "Pick": [1, 2, 3],
    "Place": [2, 3, 4],
    "Sort": [3, 4, 5]
}

Q = {}

alpha = 0.2
gamma = 0.9

for task, states in tasks.items():

    Q[task] = np.zeros(len(states))

    for episode in range(100):

        for i, state in enumerate(states):

            reward = 10 if state == states[-1] else -1

            if i < len(states) - 1:
                next_value = np.max(Q[task][i + 1:])
            else:
                next_value = 0

            Q[task][i] += alpha * (
                reward + gamma * next_value - Q[task][i]
            )

print("Learned policies:")

for task in Q:
    print(task, ":", Q[task])
