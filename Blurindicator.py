##
##  Blur indicator
##

from PIL import Image as pim
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

def b(image):
    if( isinstance(image, pim.Image) ):
        image = numpy.array(image)
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    value = cv.Laplacian(image, cv.CV_64F).var()
    return(value)

resize = (256, 256)
image = pim.open(sample('image', 1)).resize(resize)
image
value = b(image)
value
