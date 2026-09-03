import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model

state_size = 4
action_size = 2

inputs = Input(shape=(state_size,))

x = Dense(32, activation="relu")(inputs)

value = Dense(1)(x)

advantage = Dense(action_size)(x)

q_values = value + (
    advantage -
    tf.reduce_mean(advantage, axis=1, keepdims=True)
)

model = Model(inputs, q_values)

model.compile(
    optimizer="adam",
    loss="mse"
)

print(model.summary())

print("Dueling DQN model created successfully.")
