import cv2
import numpy as np


# Defining our low pass filter
def low_pass_filter(img):
    sigma_x = 0
    sigma_y = 0
    kernel_size = 21
    kernel_size = (kernel_size, kernel_size)
    return cv2.GaussianBlur(img, kernel_size, sigmaX=sigma_x, sigmaY=sigma_y)


# Defining our high pass filter + substracting the low frequencies form the image
def high_pass_filter(img):
    low_frequencies = low_pass_filter(img)
    return cv2.subtract(img, low_frequencies)


# Merging the low and the high frequencies together
def merge_frequencies(low_f, high_f):
    return cv2.add(low_f, high_f)


# Create window depending on the size of the picture
def show_image(img):
    height, width = img.shape[:2]
    title = 'Hybrid image'
    cv2.namedWindow(title, cv2.WINDOW_GUI_EXPANDED)
    cv2.moveWindow(title, 0, 0)
    cv2.resizeWindow(title, width, height)


    # Checking for user keyboard input:
    # + to enlarge the size of the picrue
    # - to reduce the size of the picrue
    # q to quit (stop the program)
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


# Function to get the positions from user input
def warp_image(img_1, img_2):
    points_img_1 = []
    points_img_2 = []


    # Await l-mouse click input from user to select the cords and draw blue circles arround the selected spot
    # This function works only for img_1 and accepts only three inputs
    def click_img_1(event, x, y, flags, param):
        pos = len(points_img_1)
        if event == cv2.EVENT_LBUTTONDOWN and pos < 3:
            points_img_1.append((x, y))
            cv2.circle(img_1, points_img_1[pos], 10, (255, 0, 0), 2)
            cv2.imshow('img1', img_1)


    # Await l-mouse click input from user to select the cords and draw blue circles arround the selected spot
    # This function works only for img_2 and accepts only three inputs
    def click_img_2(event, x, y, flags, param):
        pos = len(points_img_2)
        if event == cv2.EVENT_LBUTTONDOWN and pos < 3:
            points_img_2.append((x, y))
            cv2.circle(img_2, points_img_2[pos], 10, (255, 0, 0), 2)
            cv2.imshow('img2', img_2)

    # Create a copy of the images
    img_1_copy = img_1.copy()
    img_2_copy = img_2.copy()
    
    # Name windows accordingly and set MousCallback on the specific windows
    cv2.namedWindow('img1')
    cv2.namedWindow('img2')
    cv2.setMouseCallback('img1', click_img_1)
    cv2.setMouseCallback('img2', click_img_2)

    # Calculate the affine transformation - Transform the second image to fit the selected cords
    while True:
        if len(points_img_1) == 3 and len(points_img_2) == 3:
            T_affine = cv2.getAffineTransform(np.float32(points_img_2), np.float32(points_img_1))
            img_2 = cv2.warpAffine(img_2_copy, T_affine, img_2_copy.shape[:2], borderValue=(255, 255, 255))
            points_img_1 = []
            points_img_2 = []
            img_1 = img_1_copy.copy()
            img_2_copy = img_2.copy()
        
        # Show images
        cv2.imshow('img1', img_1)
        cv2.imshow('img2', img_2)
        key = cv2.waitKey(10)
        if key == ord('\r'):
            cv2.destroyAllWindows()
            break
    
    return img_2


# Start of the program
def main():
    # Read the two images
    img_1 = cv2.imread('images/set_1/angry_man.png', cv2.IMREAD_COLOR)
    img_2 = cv2.imread('images/set_1/woman.png', cv2.IMREAD_COLOR)
    
    # Resize the images to 600x600 pixel
    img_1 = cv2.resize(img_1, (600, 600))
    img_2 = cv2.resize(img_2, (600, 600))

    # Call wrap_image function to await position input from the user
    img_2 = warp_image(img_1.copy(), img_2.copy())

    # Extract the frequencies
    low_frequencies = low_pass_filter(img_1)
    high_frequencies = high_pass_filter(img_2)

    # Merge the low frequencies of img_1 together with the high_frequencies of img_2
    hybrid_image = merge_frequencies(low_frequencies, high_frequencies)
    
    # Show modified (calculated) image
    show_image(hybrid_image)


if __name__ == '__main__':
    main()
