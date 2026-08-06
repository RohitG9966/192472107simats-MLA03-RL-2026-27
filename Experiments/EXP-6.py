# Experiment 6: SARSA

alpha = 0.5
gamma = 0.9

Q = [[0, 0], [0, 0], [0, 0]]
rewards = [0, 5, 10]

for episode in range(10):
    state = 0
    action = 0

    while state < 2:
        next_state = state + 1
        next_action = 0
        reward = rewards[next_state]

        Q[state][action] += alpha * (
            reward + gamma * Q[next_state][next_action] - Q[state][action]
        )

        state = next_state
        action = next_action

print("SARSA Q Table:")
for row in Q:
    print(row)