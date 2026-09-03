import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

state_size = 4
action_size = 2

model = Sequential([
    Dense(24, activation="relu", input_shape=(state_size,)),
    Dense(24, activation="relu"),
    Dense(action_size, activation="linear")
])

model.compile(
    optimizer="adam",
    loss="mse"
)

for episode in range(100):

    state = np.random.rand(1, state_size)

    action = np.argmax(model.predict(state, verbose=0)[0])

    reward = np.random.choice([-1, 1])

    next_state = np.random.rand(1, state_size)

    target = reward + 0.9 * np.max(
        model.predict(next_state, verbose=0)[0]
    )

    target_values = model.predict(state, verbose=0)
    target_values[0][action] = target

    model.fit(state, target_values, epochs=1, verbose=0)

print("DQN training completed.")
