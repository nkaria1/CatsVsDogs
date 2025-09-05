from os import listdir
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

folder = 'train/'

photos, labels = [],[]

for file in listdir(folder):
    label=0
    if file.startswith('cat'):
        label=1
    photo = load_img(folder +file, target_size=(200,200))
    photos.append(img_to_array(photo))
    labels.append(label)

photos = np.asarray(photos)
labels = np.asarray(labels)

print(photos.shape, labels.shape)

np.save('cat_and_dog_photo_array.npy', photos)
np.save('cat_and_dog_labels_array.npy', labels)


