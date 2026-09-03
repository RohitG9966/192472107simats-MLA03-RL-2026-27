import numpy as np

states = ["Low", "Medium", "High"]
actions = ["Decrease", "Maintain", "Increase"]

Q = np.zeros((3, 3))

alpha = 0.1
gamma = 0.9

for episode in range(100):

    state = np.random.randint(3)

    for step in range(20):

        action = np.random.randint(3)

        if action == 0:
            next_state = max(0, state - 1)
            reward = 5
        elif action == 1:
            next_state = state
            reward = 2
        else:
            next_state = min(2, state + 1)
            reward = -3

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

print("Learned Q-table:")
print(Q)

print("\nOptimal Energy Actions:")
for i, state in enumerate(states):
    print(state, "->", actions[np.argmax(Q[i])])
