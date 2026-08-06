episodes = [
    [1, 2, 3],
    [2, 3],
    [1, 3]
]

returns = {}

for ep in episodes:
    G = sum(ep)
    for state in ep:
        returns.setdefault(state, []).append(G)

print("State Values")
for state in returns:
    print("State", state, "=", sum(returns[state]) / len(returns[state]))