import cv2
import numpy as np


def low_pass_filter(img, kernel_size):
    sigma_x = 0
    sigma_y = 0
    kernel_size = (kernel_size, kernel_size)
    return cv2.GaussianBlur(img, kernel_size, sigmaX=sigma_x, sigmaY=sigma_y)


def high_pass_filter(img, kernel_size):
    low_frequencies = low_pass_filter(img, kernel_size)
    return np.subtract(img, low_frequencies) + 127


def merge_frequencies(low_f, high_f):
    gamma = -127
    weight_low_f = 1
    weight_high_f = 1
    return cv2.addWeighted(low_f, weight_low_f, high_f, weight_high_f, gamma)


def show_image(img):
    height, width = img.shape[:2]
    title = 'Hybrid image'
    cv2.namedWindow(title, cv2.WINDOW_GUI_EXPANDED)
    cv2.moveWindow(title, 0, 0)
    cv2.resizeWindow(title, width, height)

    while True:
        cv2.imshow(title, img)
        key = cv2.waitKey(0)
        if key == ord('-'):
            width -= 5
            height -= 5
            cv2.resizeWindow(title, width, height)
        if key == ord('+'):
            width += 5
            height += 5
            cv2.resizeWindow(title, width, height)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()


def main():
    img_1 = cv2.imread('data/images/angry_man.png', cv2.IMREAD_COLOR)
    img_2 = cv2.imread('data/images/woman.png', cv2.IMREAD_COLOR)

    kernel_size = 33
    low_frequencies = low_pass_filter(img_1, kernel_size)
    high_frequencies = high_pass_filter(img_2, kernel_size)

    hybrid_image = merge_frequencies(low_frequencies, high_frequencies)
    show_image(hybrid_image)


if __name__ == '__main__':
    main()
