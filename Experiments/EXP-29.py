import numpy as np

states = ["Low Traffic", "Medium Traffic", "High Traffic"]
actions = ["Short Green", "Long Green"]

Q = np.zeros((3, 2))

alpha = 0.1
gamma = 0.9

for episode in range(200):

    state = np.random.randint(3)

    for step in range(20):

        action = np.argmax(Q[state])

        if np.random.rand() < 0.2:
            action = np.random.randint(2)

        if action == 0:
            reward = -5 if state == 2 else 2
        else:
            reward = 5 if state == 2 else 1

        next_state = np.random.randint(3)

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

print("Traffic Signal Policy:")

for i in range(3):
    print(
        states[i],
        "->",
        actions[np.argmax(Q[i])]
    )
