
from timeit import default_timer as timer
import cv2
from scipy import ndimage

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












