alpha = 0.5
gamma = 0.9

V = [0, 0, 0]
reward = [0, 5, 10]

for i in range(10):
    V[0] += alpha * (reward[1] + gamma * V[1] - V[0])
    V[1] += alpha * (reward[2] + gamma * V[2] - V[1])

print("State Values:")
for i in range(3):
    print("State", i, "=", round(V[i], 2))