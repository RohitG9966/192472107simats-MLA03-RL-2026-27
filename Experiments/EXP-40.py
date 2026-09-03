import numpy as np

states = [
    "Weak",
    "Average",
    "Good"
]

actions = [
    "Easy Lesson",
    "Normal Lesson",
    "Advanced Lesson"
]

Q = np.zeros((3, 3))

alpha = 0.1
gamma = 0.9

for episode in range(200):

    state = np.random.randint(3)

    for step in range(20):

        if np.random.rand() < 0.2:
            action = np.random.randint(3)
        else:
            action = np.argmax(Q[state])

        # Reward suitable learning content
        if state == 0 and action == 0:
            reward = 10
        elif state == 1 and action == 1:
            reward = 10
        elif state == 2 and action == 2:
            reward = 10
        else:
            reward = -2

        next_state = min(
            2,
            max(0, state + np.random.choice([-1, 0, 1]))
        )

        Q[state, action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state, action]
        )

        state = next_state

print("Personalized Education RL Training Completed.\n")

for i in range(3):
    print(
        states[i],
        "->",
        actions[np.argmax(Q[i])]
    )
