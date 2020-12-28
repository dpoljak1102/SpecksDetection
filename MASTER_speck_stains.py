from timeit import default_timer as timer
import cv2
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
#%%

def DetectionSpecks(image):  
    start = timer()  
    gray_image = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray_image, (7,7), 0)
    thresh = cv2.adaptiveThreshold(gaussian_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 99, 6)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    blob = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    blob_2 = cv2.morphologyEx(blob, cv2.MORPH_CLOSE, kernel)
    min_filter = ndimage.minimum_filter(blob_2 , size=15,  mode='nearest')
    #Inverting image becouse of regionprops
    invert_image = cv2.bitwise_not(min_filter)  
    end = timer() 
    return invert_image,  round(end-start, 4);

def DetectionStains(image):
    return 0

def fourierTransform(image, mask):
    #Fourier Transform
    image_ft = np.fft.fft2(image)
    #Shift center from top left conter to center
    image_ft_shift = np.fft.fftshift(image_ft)
    #Mask
    image_ft_shift_m = image_ft_shift*mask
    #Inverse image
    image_inverse = np.fft.ifft2(image_ft_shift_m)
    return np.abs(image_inverse)

"""
# =============================================================================
#  Masks(filters)
# =============================================================================
"""
def Gaussian(image, x, y):
    sigmax, sigmay = x, y
    rows, cols = image.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    x = np.linspace(0,rows, rows)
    y = np.linspace(0,cols, cols)
    X,Y = np.meshgrid(x[0], y[0])
    mask = np.exp(-(((X-ccol)/sigmax)**2 + ((Y-crow)/sigmay)**2))
    return mask

def BPF(image, out_radius,in_radius):
    rows, cols = image.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.zeros((rows, cols), np.uint8)
    r_out = out_radius
    r_in = in_radius
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
    mask[mask_area] = 255
    return mask

def HPF(image, radius):
    rows, cols = image.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.ones((rows, cols), np.uint8)
    r = radius
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 200
    return mask

def LPF(image, radius): 
    rows, cols = image.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.zeros((rows, cols), np.uint8)
    r = radius
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r 
    mask[mask_area] = 1
    return mask

def ShowGray(name):
    plt.figure(figsize=(20,20))
    plt.imshow(name, cmap='gray')
    plt.show()

def Counter(image):
    image_label = measure.label(image, background=0)
    propsa = measure.regionprops(image_label)
    length = len(propsa)
    return length-1

