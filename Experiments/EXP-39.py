import numpy as np

states = [
    "Low Patients",
    "Medium Patients",
    "High Patients"
]

actions = [
    "Normal Resources",
    "Increase Resources"
]

Q = np.zeros((3, 2))

alpha = 0.1
gamma = 0.9

for episode in range(200):

    state = np.random.randint(3)

    for step in range(20):

        if np.random.rand() < 0.2:
            action = np.random.randint(2)
        else:
            action = np.argmax(Q[state])

        if state == 2 and action == 1:
            reward = 10
        elif state == 2 and action == 0:
            reward = -10
        else:
            reward = 5

        next_state = np.random.randint(3)

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

print("Healthcare RL training completed.\n")

for i in range(3):
    print(
        states[i],
        "->",
        actions[np.argmax(Q[i])]
    )
