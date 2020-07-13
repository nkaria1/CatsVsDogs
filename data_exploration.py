import matplotlib.pyplot as plt
from matplotlib.image import imread
import cv2

folder = 'train/'

def display_images():
    for i in range(9):
        plt.subplot(330 +i +1)
        filename = folder + 'dog.' + str(i) + '.jpg'
        image = imread(filename)
        plt.imshow(image)
    plt.show()

def resize_images():
    pass

if __name__ == '__main__':
    display_images()
