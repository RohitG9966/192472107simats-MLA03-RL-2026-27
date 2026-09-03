import numpy as np

states = ["Unknown", "Left", "Right", "Goal"]
actions = ["Left", "Right", "Forward"]

Q = np.zeros((4, 3))

alpha = 0.1
gamma = 0.9

for episode in range(200):

    state = 0

    for step in range(20):

        action = np.random.randint(3)

        if action == 0:
            next_state = max(0, state - 1)
        elif action == 1:
            next_state = min(3, state + 1)
        else:
            next_state = min(3, state + 1)

        reward = 10 if next_state == 3 else -1

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

        if state == 3:
            break

print("POMDP Robot Training Completed.")

for i in range(4):
    print(
        states[i],
        "->",
        actions[np.argmax(Q[i])]
    )
