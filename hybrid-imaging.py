import cv2
import numpy as np

def low_pass_filter(img):
    print()

def high_pass_filter(img):
    print()

def merge_images(img_1, img_2):
    print()

def main():
    img_1 = cv2.imread('data/images/angry_man.png')
    img_2 = cv2.imread('data/images/woman.png')

    low_f_img = low_pass_filter(img_1)
    high_f_img = high_pass_filter(img_2)

    hybrid_image = merge_images(low_f_img, high_f_img)

    title = 'Hybrid image'
    cv2.namedWindow(title)
    cv2.imshow(title, hybrid_image)

if __name__ == '__main__':
    main()
