import numpy as np

states = ["A", "B", "C", "D", "Goal"]

Q = np.zeros((5, 2))

alpha = 0.1
gamma = 0.9

for episode in range(200):

    state = 0

    for step in range(20):

        action = np.random.randint(2)

        if action == 0:
            next_state = min(state + 1, 4)
            reward = 5
        else:
            next_state = max(state - 1, 0)
            reward = -1

        if next_state == 4:
            reward = 20

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

        if state == 4:
            break

print("Optimal Road Policy:")

for i in range(5):
    print(
        states[i],
        "-> Action",
        np.argmax(Q[i])
    )
