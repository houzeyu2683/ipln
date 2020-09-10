##
##  Gaussian noise
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

def gn(image, mu=0, sigma=1, array=False):
    image = numpy.array(image)
    shape = image.shape
    noise = numpy.random.normal(mu, sigma, shape)
    noise = noise.reshape(shape)
    output = image + noise
    if(array):
        return(output)
    else:
        output = numpy.around(output).astype('uint8')
        output = im.fromarray(output)
        return(output)

resize = (256, 256)
old = im.open(sample('image', 1)).resize(resize)
old
new = gn(old,  mu=0, sigma=10)
new

# def noisy(noise_typ,image):
#    if noise_typ == "gauss":
#       row,col,ch= image.shape
#       mean = 0
#       var = 0.1
#       sigma = var**0.5
#       gauss = np.random.normal(mean,sigma,(row,col,ch))
#       gauss = gauss.reshape(row,col,ch)
#       noisy = image + gauss
#       return noisy
