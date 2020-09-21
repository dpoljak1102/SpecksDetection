
import matplotlib.pyplot as plt
from skimage import measure
import cv2
import os

#%%
from MASTER_report import CreateFolders
from MASTER_report import Report

from MASTER_speck_stains import DetectionSpecks, DetectionStains

#%%

def ShowGray(name):
    plt.figure(figsize=(20,20))
    plt.imshow(name, cmap='gray')
    plt.show()


def Counter(image):
    image_label = measure.label(image, background=0)
    propsa = measure.regionprops(image_label)
    length = len(propsa)
    return length-1




#%%
images_path= "C:/Users/Deni/Desktop/workOrqa/zadatak3/Specks test/Dirty/"


CreateFolders()

#%%
file_report = open(os.path.join(os.path.abspath(os.getcwd()),"Report_speck_stains.txt"),"w+")
for index, image in enumerate(os.listdir(images_path)):
    if image.endswith('.png'):
        image_name, image_extension = os.path.splitext(image)
        
        read_image = cv2.imread(images_path + image)
        result_image, time = DetectionSpecks(read_image)
        number_speck = Counter(result_image)
        
        
        #def __init__(self, image_name, image_extension, number_speck, number_stains, time):
        
        image_report = Report(image_name, image_extension, number_speck, 0, time)
        #image_report.ImageReportSpeck(result_image)
        
        print("File {}  Time : {} Status: {}".format(index+1, time, image_report.Status()))
        
        file_report.write(image_report.WriteReport())
        
    else:
        raise Exception("Something went wrong with image extension change to (PNG)")

file_report.close()