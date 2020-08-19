##
##  Sharpness
##

from PIL import ImageEnhance as ime
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

def s(image, threshold=1, array=False):
    try:
        image = im.fromarray(image)
    except:
        pass
    enhancer = ime.Sharpness(image)
    output = enhancer.enhance(threshold)
    if(array):
        output = numpy.array(output)
        return(output)
    else:
        return(output)

resize = (256, 256)
old = im.open(sample('image', 1)).resize(resize)
old
new = s(old, threshold=20)
new
