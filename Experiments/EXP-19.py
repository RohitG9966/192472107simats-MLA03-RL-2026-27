import numpy as np

robots = 3
states = 5
actions = 2

Q = np.zeros((robots, states, actions))

alpha = 0.1
gamma = 0.9

for episode in range(100):

    for robot in range(robots):

        state = np.random.randint(states)

        for step in range(20):

            action = np.argmax(Q[robot, state])

            if np.random.rand() < 0.2:
                action = np.random.randint(actions)

            next_state = min(state + 1, states - 1)

            reward = 10 if next_state == states - 1 else -1

            Q[robot, state, action] += alpha * (
                reward +
                gamma * np.max(Q[robot, next_state]) -
                Q[robot, state, action]
            )

            state = next_state

print("Multi-Agent Q-learning completed.")

for robot in range(robots):
    print("\nRobot", robot + 1)
    print(Q[robot])
