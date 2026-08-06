# Experiment 4: Policy Iteration

states = ["A", "B", "Goal"]

policy = {
    "A": "Move to B",
    "B": "Move to Goal",
    "Goal": "Stop"
}

print("Optimal Policy\n")

for state in states:
    print(state, "->", policy[state])