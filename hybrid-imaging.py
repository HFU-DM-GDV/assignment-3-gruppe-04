import cv2
import numpy as np

def low_pass_filter(img):
    print()

def high_pass_filter(img):
    print()

def main():
    img_1 = cv2.imread('data/images/angry_man.png')
    img_2 = cv2.imread('data/images/woman.png')

    low_f_img = low_pass_filter(img_1)
    high_f_img = high_pass_filter(img_2)

    

if __name__ == '__main__':
    main()
