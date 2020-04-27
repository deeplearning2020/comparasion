import os
import cv2
import time



def prepare_images(path):
    for file in os.listdir(path):
        img = cv2.imread(path + '/' + file)
        print(img.shape)
        h, w, _ = img.shape
        new_height = 256
        new_width = 256
        img = cv2.resize(img, (int(new_width), int(new_height)), interpolation = cv2.INTER_LINEAR)
        print('Saving {}'.format(file))
        time.sleep(0.1)
        os.remove(os.path.join(path, file))
        time.sleep(0.2)
        cv2.imwrite((write_path + file), img)
        time.sleep(0.2)

new_path = os.path.join(os.getcwd(),'new')
write_path = os.path.join(os.getcwd(), 'new/')
print(write_path)
prepare_images(new_path)

