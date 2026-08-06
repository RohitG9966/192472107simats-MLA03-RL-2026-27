# Experiment 1: Simplified Chess MDP

states = ["Start", "Middle", "Winning", "Losing", "Goal"]

actions = {
    "Start": ["Attack", "Defend"],
    "Middle": ["Attack", "Defend"],
    "Winning": ["Finish"],
    "Losing": ["Recover"],
    "Goal": []
}

transitions = {
    ("Start", "Attack"): ("Middle", 5),
    ("Start", "Defend"): ("Losing", -2),
    ("Middle", "Attack"): ("Winning", 10),
    ("Middle", "Defend"): ("Losing", -3),
    ("Winning", "Finish"): ("Goal", 20),
    ("Losing", "Recover"): ("Middle", 2)
}

state = "Start"
total_reward = 0

print("Initial State:", state)

while state != "Goal":
    action = actions[state][0]
    next_state, reward = transitions[(state, action)]
    print(f"{state} --{action}--> {next_state} Reward={reward}")
    total_reward += reward
    state = next_state

print("\nGoal Reached!")
print("Total Reward =", total_reward)