import numpy as np

states = ["Unknown", "Victim", "Obstacle", "Safe"]
actions = ["Move", "Search", "Rescue"]

Q = np.zeros((len(states), len(actions)))

alpha = 0.1
gamma = 0.9

for episode in range(100):

    state = np.random.randint(len(states))

    for step in range(20):

        action = np.argmax(Q[state])

        if np.random.rand() < 0.2:
            action = np.random.randint(len(actions))

        if action == 0:
            next_state = np.random.randint(len(states))
            reward = 1

        elif action == 1:
            next_state = 1
            reward = 5

        else:
            next_state = 3
            reward = 10

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

print("POMDP learning completed.")
print("\nLearned Q-table:")
print(Q)

print("\nBest actions:")
for i, state in enumerate(states):
    print(state, "->", actions[np.argmax(Q[i])])
