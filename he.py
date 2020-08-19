##
##  Histogram equalization
##

from PIL import Image as im
import cv2 as cv
import os
import random
import numpy

def sample(folder, size):
    file = random.sample(os.listdir(folder), size)
    output = [os.path.join(folder, i) for i in file]
    if(size==1):
        output = output[0]
    return(output)

def he(image, array=False):
    image = numpy.array(image)
    origin = image.copy()
    convert = cv.cvtColor(image,cv.COLOR_BGR2YCR_CB)
    channel=cv.split(convert)
    cv.equalizeHist(channel[0],channel[0])
    cv.merge(channel, convert)
    cv.cvtColor(convert, cv.COLOR_YCR_CB2BGR, image)
    if(array):
        return(image)
    else:
        image = im.fromarray(image)
        return(image)


resize = (256, 256)
old = im.open(sample('image', 1)).resize(resize)
old
new = he(old)
new


#
# i = 0
# link = sample('image', 20)[i]
# resize = (128, 128)
#
# image = PIL.Image.open(link).resize(resize)
# image = numpy.array(image)
# convert = cv.cvtColor(image,cv.COLOR_BGR2YCR_CB)
# channel=cv.split(convert)
# cv.equalizeHist(channel[0],channel[0])
# cv.merge(channel, convert)
# cv.cvtColor(convert, cv.COLOR_YCR_CB2BGR, image)
# PIL.Image.fromarray(image)
#
#
# cv.imread(link)
#
#
# def hisEqulColor(img):
#
#     channels=cv2.split(ycrcb)
#     print len(channels)
#     cv2.equalizeHist(channels[0],channels[0])
#     cv2.merge(channels,ycrcb)
#     cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR,img)
#     return img
