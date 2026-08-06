# Experiment 11: Simple Deep Q Network

import random

Q = [0, 0, 0]

for episode in range(10):
    state = random.randint(0, 2)
    reward = state + 1
    Q[state] += 0.5 * (reward - Q[state])

print("Q Values:")
for i in range(3):
    print("State", i, "=", round(Q[i], 2))