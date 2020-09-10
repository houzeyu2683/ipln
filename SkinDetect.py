##
##  Skin detect
##

from PIL import Image as pim
import cv2
import os
import random
import numpy as np

def sample(folder, size):
    file = random.sample(os.listdir(folder), size)
    output = [os.path.join(folder, i) for i in file]
    if(size==1):
        output = output[0]
    return(output)

def sd(image):
    if( isinstance(image, pim.Image) ):
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    '''Convert color space from gbr to hsv.'''
    img_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    '''Skin color range for hsv color space'''
    HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255))
    HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    '''Convert color space from gbr to YCbCr.'''
    img_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    '''Skin color range for YCbCr color space.'''
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135))
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

    '''merge skin detection (YCbCr and hsv)'''
    global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
    global_mask=cv2.medianBlur(global_mask,3)
    global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))

    '''Result'''
    HSV_result = cv2.bitwise_not(HSV_mask)
    YCrCb_result = cv2.bitwise_not(YCrCb_mask)
    global_result=cv2.bitwise_not(global_mask)

    '''Return'''
    image = pim.fromarray(global_result)
    # value  = np.sum(global_result==0)/np.prod(global_result.shape)
    return(image)

resize = (256, 256)
old = pim.open(sample('image', 1)).resize(resize)
old
new = sd(old)
new
