# Experiment 13: Actor-Critic

state_value = 0
policy = 0.5

reward = 10

for i in range(5):
    td_error = reward - state_value
    state_value += 0.1 * td_error
    policy += 0.05 * td_error

print("State Value =", round(state_value, 2))
print("Policy =", round(policy, 2))