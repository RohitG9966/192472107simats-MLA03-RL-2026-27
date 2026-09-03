import numpy as np

states = ["Left Lane", "Middle Lane", "Right Lane"]
actions = ["Move Left", "Stay", "Move Right"]

Q = np.zeros((3, 3))

alpha = 0.1
gamma = 0.9

for episode in range(200):

    state = 1

    for step in range(20):

        action = np.random.randint(3)

        if action == 0:
            next_state = max(0, state - 1)
            reward = 2
        elif action == 1:
            next_state = state
            reward = 1
        else:
            next_state = min(2, state + 1)
            reward = 2

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

print("Autonomous vehicle training completed.")

for i in range(3):
    print(states[i], "->", actions[np.argmax(Q[i])])
