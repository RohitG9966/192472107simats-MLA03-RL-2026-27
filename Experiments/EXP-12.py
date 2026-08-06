# Experiment 12: Double Q Learning

Q1 = [0, 0, 0]
Q2 = [0, 0, 0]

reward = [2, 5, 10]

for i in range(10):
    Q1[0] += 0.5 * (reward[1] + Q2[1] - Q1[0])
    Q2[1] += 0.5 * (reward[2] + Q1[2] - Q2[1])

print("Q1 =", Q1)
print("Q2 =", Q2)