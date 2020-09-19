
import os
import cv2
import matplotlib.pyplot as plt
#%%
def CreateFolders():
    directory_name = "ImageResults"
    #Create folder witn directory_name if not exists
    if not os.path.exists(directory_name):
        try:
            subfolder_names = ["Dirty", "Clean"]
            for subfolder_name in subfolder_names:
                os.makedirs(os.path.join(directory_name, subfolder_name))
        except :
            raise Exception("Something went wrong with creating directory")
        finally:
            print("Directory", directory_name, "created")
    #If folder exists with directory_name, delete it and make new one
    else:
        try:
            shutil.rmtree(directory_name)
            os.mkdir(directory_name)
        except :
            raise Exception("Something went wrong with creating directory")
        finally:
            print("Directory", directory_name, "created")    

#%%
class Report(object):
    
    #default constructor
    def __init__(self, image_name, image_extension, number_speck, number_stains, time):
        self.image_name = image_name
        self.image_extension = image_extension
        self.number_speck = number_speck
        self.number_stains = number_stains
        self.time = time
        self.status = "Dirty" if (number_speck + number_stains) > 0 else "Clean"
          

    # General report
    def WriteReport(self):
        report = "Image name: '{}'\nImage extension: '{}'\nSpeck detected: {}\nStains detected: {}\nTime: {}\nStatus: '{}'\n".format(self.image_name, self.image_extension, self.number_speck, self.number_stains, self.time, self.status)
        return report
#TODO remove ext PNG becouse cv2 knows that we you will read real images....
    def ImageReport(self, image_result):
        path = os.path.abspath(os.getcwd())
        if(self.status != "Dirty"):
            cv2.imwrite("{}/ImageResults/Clean/Report_{}.png".format(path, self.image_name), image_result)
        else:
            cv2.imwrite("{}/ImageResults/Dirty/Report_{}.png".format(path, self.image_name), image_result)

        
        
#%%


import numpy as np
from skimage import data

image = data.astronaut()
plt.imshow(image)

obj = Report("image2", "PNG", 0, 1, 2)
obj.WriteReport()
obj.ImageReport(image)

#%%
# =============================================================================
#             TESTING
# =============================================================================

#%%
"""
def ImageReportSpecks(image_result):
    path = os.path.abspath(os.getcwd())
    cv2.imwrite("{}/{}/SpecksTested_{}".format(path,dirName,image_name), image_result, cmap = plt.cm.gray )
"""