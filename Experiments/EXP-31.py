import numpy as np

states = 9
actions = 9

Q = np.zeros((states, actions))

alpha = 0.1
gamma = 0.9
epsilon = 0.1

for episode in range(500):

    state = np.random.randint(states)

    for step in range(20):

        if np.random.rand() < epsilon:
            action = np.random.randint(actions)
        else:
            action = np.argmax(Q[state])

        next_state = np.random.randint(states)

        reward = 1 if next_state == 8 else -0.1

        if np.random.rand() < epsilon:
            next_action = np.random.randint(actions)
        else:
            next_action = np.argmax(Q[next_state])

        Q[state, action] += alpha * (
            reward +
            gamma * Q[next_state, next_action] -
            Q[state, action]
        )

        state = next_state

print("SARSA training completed.")
print("\nLearned Q-table:")
print(Q)
