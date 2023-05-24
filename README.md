### Assignment 3 Group 4 - Hybrid Imaging


In this repository, we implemented a method to produce hybrid images. To produce the hybrid image we combined one picture with low frequencies with another different image with high frequencies. To create a low frequency picture, we used the gaussian blur function , which was already implemented in OpenCV. To create a high frequency image we substracted the gaussian blurred image from the original image. 

## Project Description
A program to create hybrid images. It will use the high frequencies of the first picture and the low frequencies of the second picture to create an image that can be viewed as one or the other depending on the distance to the image.

## How to
First, you need to add the file path of the pictures you want to use. Afterward, run the code. It will display two images. Select three points in order to translate the second image to the selected points on the first image. Afterward, press Enter.

It will now display the high frequencies of the first and the low frequencies of the second image. With the "+" and "-" keys, you can make the window smaller or larger. Using the "q" key, you can close the window.

## Build with

* Python 3.11.2

## Extentions

* OpenCV-Python, v4.7.0.72
* Numpy, v1.24.2

## Link to task

[Task](/Task.md)

# Authors

Leon Haas, Yannis Dold and Robin Palmer