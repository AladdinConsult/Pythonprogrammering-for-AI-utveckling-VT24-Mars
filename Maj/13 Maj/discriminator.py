from tensorflow import keras    
from keras.models import Sequential
from keras.layers import Dense

def build_discriminator(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']):
    model = Sequential()

    # Input layer
    model.add(Dense(128,activation='relu', input_shape=(1,)))

    # Hidden layers
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))

    # Output layer
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    
    return model
