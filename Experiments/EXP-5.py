# Experiment 5: Q-Learning without NumPy

alpha = 0.5
gamma = 0.9

Q = [
    [0.0, 0.0],
    [0.0, 0.0],
    [0.0, 0.0]
]

rewards = [0, 5, 10]

for episode in range(10):
    state = 0

    while state < 2:
        action = 0
        next_state = state + 1
        reward = rewards[next_state]

        max_next = max(Q[next_state])

        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * max_next - Q[state][action]
        )

        state = next_state

print("Q Table:")
for row in Q:
    print(row)