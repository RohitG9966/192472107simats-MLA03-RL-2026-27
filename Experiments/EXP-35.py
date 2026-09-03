import numpy as np

portfolios = {
    "Portfolio A": [0.05, 0.06, 0.04, 0.07],
    "Portfolio B": [0.08, 0.07, 0.09, 0.06],
    "Portfolio C": [0.03, 0.04, 0.05, 0.04]
}

print("Portfolio Performance:\n")

for name, returns in portfolios.items():

    average = np.mean(returns)
    total = np.sum(returns)

    print(name)
    print("Average Return:", round(average, 3))
    print("Total Return:", round(total, 3))
    print()

best = max(
    portfolios,
    key=lambda x: np.mean(portfolios[x])
)

print("Best Portfolio:", best)
