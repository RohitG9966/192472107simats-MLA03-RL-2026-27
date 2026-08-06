# Experiment 14: REINFORCE

reward = [1, 2, 3]
returns = []

G = 0

for r in reversed(reward):
    G += r
    returns.insert(0, G)

print("Returns:", returns)