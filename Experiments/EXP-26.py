import numpy as np

prices = [50, 75, 100, 125]
probability = [0.8, 0.6, 0.4, 0.2]

revenue = np.zeros(4)
count = np.zeros(4)

epsilon = 0.1

for step in range(1000):

    if np.random.rand() < epsilon:
        arm = np.random.randint(4)
    else:
        average = np.divide(
            revenue,
            count,
            out=np.zeros(4),
            where=count != 0
        )
        arm = np.argmax(average)

    sale = np.random.rand() < probability[arm]

    earned = prices[arm] if sale else 0

    revenue[arm] += earned
    count[arm] += 1

print("Pricing Results:")

for i in range(4):
    print(
        "Price:", prices[i],
        "Average Revenue:",
        round(revenue[i] / count[i], 2)
    )

best = np.argmax(revenue / count)

print("\nBest Price:", prices[best])
