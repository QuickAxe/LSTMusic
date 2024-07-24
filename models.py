import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, CuDNNLSTM


class simpleModel:
    def __init__(self, inputShape):
        self.inputShape = inputShape

    def getModel(self):
        model = Sequential()

        model.add(CuDNNLSTM(256, input_shape=(1, 1), return_sequences=True))
        model.add(Dropout(0.2))

        model.add(CuDNNLSTM(256))
        model.add(Dropout(0.2))

        model.add(Dense(128, activation="relu"))
        model.add(Dropout(0.2))

        model.add(Dense(1, activation="linear"))

        optimiser = tf.keras.optimizers.Adam(learning_rate=0.003, decay=1e-5)

        model.compile(loss="mse", optimizer=optimiser, metrics=["accuracy"])

        return model


mdl = simpleModel(33)
model = mdl.getModel()

model.summary()
