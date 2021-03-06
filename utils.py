
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image


def load_image(path):
    return np.array(Image.open(path))


def plot_sample(lr, sr):
    plt.figure(figsize=(20, 10))

    images = [lr, sr]
    titles = ['LR', f'SR (x{sr.shape[0] // lr.shape[0]})']

    for i, (img, title) in enumerate(zip(images, titles)):
        #plt.subplot(1, 2, i+1)
        plt.box(on=None)
        plt.axis('off')
        plt.imshow(img)
        #plt.savefig(str(i) + ".png")
