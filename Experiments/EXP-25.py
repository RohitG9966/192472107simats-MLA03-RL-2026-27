import numpy as np

arms = 3
steps = 1000

true_rates = [0.2, 0.5, 0.8]

# Epsilon-Greedy
epsilon = 0.1
counts = np.zeros(arms)
values = np.zeros(arms)

for step in range(steps):

    if np.random.rand() < epsilon:
        arm = np.random.randint(arms)
    else:
        arm = np.argmax(values)

    reward = np.random.rand() < true_rates[arm]

    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

print("Epsilon-Greedy CTR:", round(np.mean(values), 3))

# UCB
counts = np.ones(arms)
values = np.zeros(arms)

for step in range(1, steps + 1):

    ucb = values + np.sqrt(
        2 * np.log(step + 1) / counts
    )

    arm = np.argmax(ucb)

    reward = np.random.rand() < true_rates[arm]

    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

print("UCB CTR:", round(np.mean(values), 3))

# Thompson Sampling
success = np.ones(arms)
failure = np.ones(arms)

for step in range(steps):

    samples = np.random.beta(success, failure)

    arm = np.argmax(samples)

    reward = np.random.rand() < true_rates[arm]

    if reward:
        success[arm] += 1
    else:
        failure[arm] += 1

print("Thompson Sampling completed.")
