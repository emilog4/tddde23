import cv2 as cv
from cvlib import *
from lab5a import cvimg_to_list
import random

plane_img = cv2.imread("plane.jpg")
flower_img = cv2.imread("flowers.jpg")
gradient_img = cv.imread("gradient.jpg")


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Checks if a pixel has it values between a given param
    """
    def is_black(hsv):
        if not isinstance(hsv,tuple):   
            raise TypeError("Input must be a tuple")
        if len(hsv) != 3:
            raise TypeError("Tuple must be of lenght 3")
        (h_input, s_input, v_input) = hsv
        if h_input > hlow and h_input < hhigh and \
                s_input > slow and s_input < shigh and \
                v_input > vlow and v_input < vhigh:
            return 1
        else:
            return 0
    return is_black


def generator_from_image(original_list):
    """
    Checks the pixel from an index
    """
    if type(original_list) != list:
        raise Exception("Argument is not a list")
    def check_pixel_color(pixel_index):
        if type(pixel_index) != int:
            raise TypeError("Index is not an integer")
        if pixel_index > len(original_list)-1:
            raise IndexError("Index is out of bounds")
        return original_list[pixel_index]
    return check_pixel_color

   
# Lab 3 och 4
def combine_images(mask, mask_function, image_generator1, image_generator2):
    """
    Combines 2 images

    Input:
    mask: Image to be interpreted by the mask function
    mask_function: Returns a value between 0 and 1 for any pixel value. A value of 0 means
            means use only image 1 and a value of 1 means only use image 2. A value between
            0 and 1 means use (value)*image1 + (1-value)*image2
    image_generator1: Returns a pixel value for each pixel in an image
    image_generator2: -||-

    Output:
    A new image which is a combination of image1 and 2
    """
    masked_image = []

    # for i in range(len(mask)):
    try:
        for i, obj in enumerate(mask):
            maskvalue = mask_function(obj)
            pixel1 = image_generator1(i)
            pixel2 = image_generator2(i)
            new_pixel = (pixel1[0]*maskvalue + pixel2[0]*(1-maskvalue), pixel1[1]*maskvalue +
                         pixel2[1]*(1-maskvalue), pixel1[2]*maskvalue + pixel2[2]*(1-maskvalue))
            masked_image.append(new_pixel)
        return masked_image
    except TypeError as e:
        print("You must enter a correct value", e)
        return None
    except ValueError as e:
        print("Incorrect value of argument given", e)
        return None
    except IndexError as e:
        print("List index out of range, is images the same size?",e)
        return None
    except Exception: 
        print("Something went wrong")
        return None


def gradient_condition(pixels):
    """
    Calculates the value of the amount of black in an pixel (h,s,V)
    """
    (a, b, black_pxl) = pixels
    if pixels != tuple or len(pixels) != 3 or type(a) != int or type(b) != int or type(black_pxl) != int:
        raise ValueError("Argument must be a tuple of length 3 with integers")

    return black_pxl/255
  

# Skapa en generator som gör en stjärnhimmel
def generator1(index):
    """
    Generates a mask that looks like stars
    """

    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)


def exempel1():
    sv_plane = cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(sv_plane)
    is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))
    cv2.imshow('sky', greyscale_list_to_cvimg(
        sky_pixels, sv_plane.shape[0], sv_plane.shape[1]))
    cv2.waitKey(0)


def exempel2():
    # Omvandla originalbilden till en lista med HSV-färger
    hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
    # Omvandla orginalbilden till en riktig lista
    plane_img_list = cvimg_to_list(plane_img)
    # Skapa ett filter som identifierar himlen
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)
    # Skapa en generator för den inlästa bilden
    plane_generator = generator_from_image(plane_img_list)
    # Använd combine images för att sammanfoga bilden
    result = combine_images(hsv_list, condition, generator1, plane_generator)
    # Omvandla resultatet till en riktig bild och visa upp den
    new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
    cv2.imshow('First image', new_img)
    cv2.waitKey(0)


def exempel3():
    gradient_hsv_list = cvimg_to_list(
        cv2.cvtColor(gradient_img, cv2.COLOR_BGR2HSV))
    # Omvandla orginalbilderna till en riktig lista
    plane_img_list = cvimg_to_list(plane_img)
    flower_img_list = cvimg_to_list(flower_img)
    # Skapa en generator för den inlästa bilden
    plane_generator = generator_from_image(plane_img_list)
    flower_generator = generator_from_image(flower_img_list)
    # Använd combine images för att sammanfoga bilden
    result2 = combine_images(
        gradient_hsv_list, gradient_condition, flower_generator, plane_generator)
    # Omvandla resultatet till en riktig bild och visa upp den
    new_img2 = rgblist_to_cvimg(
        result2, plane_img.shape[0], plane_img.shape[1])
    cv2.imshow('Final image', new_img2)
    cv2.waitKey(0)


if __name__ == "__main__":
    exempel1()
    exempel2()
    exempel3()
