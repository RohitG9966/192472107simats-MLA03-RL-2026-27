Q = [[0] * 4 for _ in range(4)]

reward = 10
alpha = 0.5
gamma = 0.9

state = 0

while state < 3:
    next_state = state + 1

    Q[state][0] += alpha * (
        reward + gamma * max(Q[next_state]) - Q[state][0]
    )

    state = next_state

print("Grid World Q Table:")
for row in Q:
    print(row)