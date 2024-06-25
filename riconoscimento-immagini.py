import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, InputLayer, Input, Conv2D, MaxPool2D, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.backend import clear_session
import matplotlib.pyplot as plt

# Caricare il dataset CIFAR-10
cifar10 = tf.keras.datasets.cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Definire le etichette
labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
animal_classes = [2, 3, 4, 5, 6, 7]  # bird, cat, deer, dog, frog, horse
vehicle_classes = [0, 1, 8, 9]       # airplane, automobile, ship, truck

# Creare etichette binarie: 0 per veicoli, 1 per animali
y_train_binary = np.isin(y_train, animal_classes).astype(np.int32)
y_test_binary = np.isin(y_test, animal_classes).astype(np.int32)

# Definire il modello
clear_session()

model = Sequential([
    InputLayer(input_shape=(32, 32, 3)),
    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    BatchNormalization(),
    MaxPool2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    BatchNormalization(),
    MaxPool2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Output a singolo neurone per classificazione binaria
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

# Addestrare il modello
history = model.fit(X_train, y_train_binary, epochs=10, validation_data=(X_test, y_test_binary), batch_size=64)

# Valutare il modello
test_loss, test_accuracy = model.evaluate(X_test, y_test_binary)
print(f'Test accuracy: {test_accuracy}')

# Visualizzare la perdita e l'accuratezza nel tempo
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title('Loss over epochs')

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.title('Accuracy over epochs')

plt.show()
