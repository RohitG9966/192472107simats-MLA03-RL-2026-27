import numpy as np

states = 5
actions = 3

Q = np.zeros((states, actions))

alpha = 0.1
gamma = 0.9

for episode in range(200):

    state = np.random.randint(states)

    for step in range(20):

        action = np.argmax(Q[state])

        if np.random.rand() < 0.2:
            action = np.random.randint(actions)

        next_state = np.random.randint(states)

        reward = 10 if next_state == 4 else -1

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

print("Resource gathering training completed.")

for state in range(states):
    print(
        "State", state,
        "Best Action:", np.argmax(Q[state])
    )
