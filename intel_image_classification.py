# -*- coding: utf-8 -*-
"""Intel_Image_Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GwStVqMUHgiktPX0m_PuCPbMASUsiBwV
"""

from google.colab import drive
drive.mount('/content/drive')

!ls "/content/drive/My Drive"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread
import cv2
import random
from os import listdir
from sklearn.preprocessing import  LabelBinarizer
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array, array_to_img
from keras.optimizers import Adam
from PIL import Image
from keras.models import Sequential
from keras.layers import BatchNormalization, Conv2D, MaxPooling2D, Activation, Flatten, Dropout, Dense, LeakyReLU
from sklearn.model_selection import train_test_split

!apt-get install unrar

#/content/drive/MyDrive/Data science/project-13/Data.rar
!unrar x "/content/drive/MyDrive/Data science/project-13/Data.rar" "/content/drive/MyDrive/Data science/project-13/"

!ls "/content/drive/MyDrive/Data science/project-13/Data/Intel Image Dataset"

plt.figure(figsize=(11,11))
path = "/content/drive/MyDrive/Data science/project-13/Data/Intel Image Dataset/buildings"
for i in range(1,26):
    plt.subplot(5,5,i)
    plt.tight_layout()
    rand_img = imread(path +'/'+ random.choice(sorted(listdir(path))))
    plt.imshow(rand_img)
    plt.title('mountain')
    plt.xlabel(rand_img.shape[1], fontsize = 10)
    plt.ylabel(rand_img.shape[0], fontsize = 10)

dir = "/content/drive/MyDrive/Data science/project-13/Data/Intel Image Dataset"
root_dir = listdir(dir)
image_list, label_list = [], []

dir

for directory in root_dir:
  for files in listdir(f"{dir}/{directory}"):
    image_path = f"{dir}/{directory}/{files}"
    image = Image.open(image_path)
    image = image.resize((150,150))
    image = img_to_array(image)
    image_list.append(image)
    label_list.append(directory)

label_counts = pd.DataFrame(label_list).value_counts()
label_counts

num_classes = len(label_counts)
num_classes

np.array(image_list).shape

label_list = np.array(label_list)
label_list.shape

x_train, x_test, y_train, y_test = train_test_split(image_list, label_list, test_size=0.2, random_state = 10)

x_train = np.array(x_train, dtype=np.float16) / 225.0
x_test = np.array(x_test, dtype=np.float16) / 225.0
x_train = x_train.reshape( -1, 150,150,3)
x_test = x_test.reshape( -1, 150,150,3)

lb = LabelBinarizer()
y_train = lb.fit_transform(y_train)
y_test = lb.fit_transform(y_test)
print(lb.classes_)

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = 0.2)

model = Sequential([
        Conv2D(16, kernel_size = (3,3), input_shape = (150,150,3)),
        BatchNormalization(),
        LeakyReLU(),

        Conv2D(32, kernel_size = (3,3)),
        BatchNormalization(),
        LeakyReLU(),
        MaxPooling2D(5,5),

        Conv2D(64, kernel_size = (3,3)),
        BatchNormalization(),
        LeakyReLU(),

        Conv2D(128, kernel_size = (3,3)),
        BatchNormalization(),
        LeakyReLU(),
        MaxPooling2D(5,5),

        Flatten(),

        Dense(64),
        Dropout(rate = 0.2),
        BatchNormalization(),
        LeakyReLU(),

        Dense(32),
        Dropout(rate = 0.2),
        BatchNormalization(),
        LeakyReLU(),

        Dense(16),
        Dropout(rate = 0.2),
        BatchNormalization(),
        LeakyReLU(1),

        Dense(6, activation = 'softmax')
        ])
model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer = Adam(0.0005),metrics=['accuracy'])

epochs = 70
batch_size = 128
history = model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs, validation_data = (x_val, y_val))

model.save("/content/drive/MyDrive/Data science/project-13/model.keras")

plt.figure(figsize=(12, 5))
plt.plot(history.history['accuracy'], color='r')
plt.plot(history.history['val_accuracy'], color='b')
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.legend(['train', 'val'])
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(history.history['loss'], color='r')
plt.plot(history.history['val_loss'], color='b')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['train', 'val'])
plt.show()

scores = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {scores[1]*100}")

y_pred = model.predict(x_test)

img = array_to_img(x_test[1])
img

labels = lb.classes_
print(labels)
print("Originally : ",labels[np.argmax(y_test[1])])
print("Predicted : ",labels[np.argmax(y_pred[1])])

