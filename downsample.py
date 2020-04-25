import os
import cv2
import time


def down(path, factor):
    for file in os.listdir(path):
        time.sleep(0.1)
        img = cv2.imread(path + '/' + file)
        print(img.shape)
        h, w, _ = img.shape
        new_height = h / factor
        new_width = w / factor
        img = cv2.resize(img, (int(new_width), int(new_height)), interpolation = cv2.INTER_LINEAR)
        img = cv2.resize(img, (w, h), interpolation = cv2.INTER_LINEAR)
        time.sleep(0.2)
        print('Saving {}'.format(file))
        print(file)
        cv2.imwrite((write_path + 'LR.png'), img)
        time.sleep(0.2)

new_path = os.path.join(os.getcwd(),'demo')
write_path = os.path.join(os.getcwd(), 'demo/')
print(write_path)
down(new_path, 4)
