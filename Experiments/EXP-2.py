# Experiment 2: Grid World

grid = [
    ['S', '.', '.'],
    ['.', '#', '.'],
    ['.', '.', 'G']
]

row, col = 0, 0
goal = (2, 2)

moves = ['Right', 'Right', 'Down', 'Down']

print("Starting Position:", (row, col))

for move in moves:
    if move == "Right":
        col += 1
    elif move == "Left":
        col -= 1
    elif move == "Up":
        row -= 1
    elif move == "Down":
        row += 1

    print(f"Move: {move} -> Position: ({row},{col})")

if (row, col) == goal:
    print("Goal Reached!")
else:
    print("Goal Not Reached")