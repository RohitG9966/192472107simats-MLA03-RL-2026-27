# Experiment 15: Advantage Actor-Critic

reward = 10
value = 7

advantage = reward - value

policy = 0.5
policy += 0.1 * advantage

print("Advantage =", advantage)
print("Updated Policy =", round(policy, 2))