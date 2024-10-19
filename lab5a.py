import cv2 as cv
from cvlib import *
import math
import numpy as np

#  Lab 5a1

def cvimg_to_list(img):
    """
    Creates a python list from open cv list
    """
    mylist = []
    for i in range(len(img)):
        for j in img[i]:
            mylist.append(j)
    return mylist


# Lab 5a2
def blur(x, y):
    pi = math.pi
    e = math.e
    s = 4.5
    return -1/((2*pi*s**2)*e**((x**2+y**2)/(2*s**2)))


def unsharp_masking(N):
    """
    Sharpens an image using unsharp masking
    """
    return np.array([[1.5 if (x, y) == (0, 0) else blur(x, y) 
    for x in range(math.ceil(-N/2), math.ceil(N/2+1))] 
    for y in range(math.ceil(-N/2), math.ceil(N/2+1))])


def exempel1():
    img = cv2.imread('plane.jpg')
    list_img = cvimg_to_list(img)
    converted_img = rgblist_to_cvimg(
        list_img, img.shape[0], img.shape[1])    # Bildens dimensioner
    cv2.imshow("converted", converted_img)
    cv2.waitKey(0)


def exempel2():
    img = cv2.imread('plane.jpg')
    kernel = numpy.array(unsharp_masking(100))
    filtered_img = cv2.filter2D(img, -1, kernel)
    cv2.imshow("filtered", filtered_img)
    cv2.waitKey(0)

if __name__ == "__main__":
    exempel1()
    exempel2()
    
    