# Experiment 3: Value Iteration

gamma = 0.9
reward = [-1, -1, 10]

values = [0, 0, 0]

for i in range(10):
    new_values = values.copy()
    for s in range(2):
        new_values[s] = reward[s] + gamma * values[s + 1]
    new_values[2] = reward[2]
    values = new_values

print("Optimal State Values:")
for i, v in enumerate(values):
    print(f"State {i}: {round(v,2)}")