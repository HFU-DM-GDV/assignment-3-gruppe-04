import cv2
import numpy as np

def low_pass_filter(img):
    kernel_size = 33
    sigma = -1
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = np.transpose(kernel) * kernel
    print('Kernel: ', kernel)
    return cv2.filter2D(img, -1, kernel)

def high_pass_filter(img):
    kernel_size = 33
    sigma = -1
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = np.transpose(kernel) * kernel
    i_kernel = (1 - kernel)
    i_kernel = i_kernel / i_kernel.sum()
    print('Inverse Kernel: ', i_kernel)
    return cv2.filter2D(img, -1, i_kernel)

def merge_images(img_1, img_2):
    return cv2.addWeighted(img_1, 0.5, img_2, 0.5, 0)

def main():
    img_1 = cv2.imread('data/images/angry_man.png')
    img_2 = cv2.imread('data/images/woman.png')

    low_f_img = low_pass_filter(img_1)
    high_f_img = high_pass_filter(img_2)

    hybrid_image = merge_images(low_f_img, high_f_img)

    title = 'Hybrid image'
    cv2.namedWindow(title, cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow(title, hybrid_image)

    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
