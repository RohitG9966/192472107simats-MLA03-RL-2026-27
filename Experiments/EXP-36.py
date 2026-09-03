import numpy as np

tasks = {
    "Main Task": ["Move", "Collect", "Return"],
    "Move": ["Forward", "Turn"],
    "Collect": ["Pick", "Store"],
    "Return": ["Move Home"]
}

Q = {}

for task in tasks:
    Q[task] = np.zeros(len(tasks[task]))

alpha = 0.1
gamma = 0.9

for episode in range(100):

    for task, subtasks in tasks.items():

        for i in range(len(subtasks)):

            reward = 10 if i == len(subtasks) - 1 else -1

            Q[task][i] += alpha * (
                reward - Q[task][i]
            )

print("MAXQ Training Completed.\n")

for task in Q:
    best = np.argmax(Q[task])
    print(
        task,
        "->",
        tasks[task][best]
    )
