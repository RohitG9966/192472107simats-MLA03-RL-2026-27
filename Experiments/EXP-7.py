import random

rewards = [2, 5, 8]
counts = [0, 0, 0]
values = [0, 0, 0]

epsilon = 0.2

for i in range(20):
    if random.random() < epsilon:
        arm = random.randint(0, 2)
    else:
        arm = values.index(max(values))

    reward = rewards[arm]
    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

print("Estimated Values:")
for i in range(3):
    print("Arm", i + 1, "=", round(values[i], 2))