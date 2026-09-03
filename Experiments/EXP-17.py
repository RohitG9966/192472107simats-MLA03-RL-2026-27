import numpy as np

# Simple hierarchical environment
states = ["Start", "Room1", "Room2", "Goal"]
actions = ["move", "collect", "finish"]

Q = np.zeros((len(states), len(actions)))

alpha = 0.1
gamma = 0.9
episodes = 100

for episode in range(episodes):

    state = 0
    total_reward = 0

    for step in range(20):

        action = np.random.randint(len(actions))

        if state == 0:
            next_state = 1
            reward = -1

        elif state == 1:
            next_state = 2
            reward = 2

        elif state == 2:
            next_state = 3
            reward = 10

        else:
            next_state = 3
            reward = 0

        Q[state, action] += alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state
        total_reward += reward

        if state == 3:
            break

print("Learned Hierarchical Q-values:")
print(Q)

print("\nOptimal actions:")
for i, state in enumerate(states):
    print(state, "->", actions[np.argmax(Q[i])])
