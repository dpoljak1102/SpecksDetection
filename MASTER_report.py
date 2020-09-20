import os
import cv2
import matplotlib.pyplot as plt
import shutil

"""
# =============================================================================
# Create folders path/ImageResults/(Dirty, Clean)
# =============================================================================
"""
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
        except :
            raise Exception("Something went wrong with creating directory")
        finally:
            print("Directory", directory_name, "removed, and created new one")
            subfolder_names = ["Dirty", "Clean"]
            for subfolder_name in subfolder_names:
                os.makedirs(os.path.join(directory_name, subfolder_name))


"""
# =============================================================================
# WriteReport : Write txt file with summary for testing images
# ImageReport : Save images after applaying algoritham to detect speck and stains
#                in folders Dirty or Clean
# =============================================================================
"""
class Report(object):
    
    #default constructor
    def __init__(self, image_name, image_extension, number_speck, number_stains, time):
        self.image_name = image_name
        self.image_extension = image_extension
        self.number_speck = number_speck
        self.number_stains = number_stains
        self.time = time
        self.status = "Dirty" if (number_speck + number_stains) > 0 else "Clean"
          
    #JUST FOR TESTING
    def Status(self):
        return self.status

    # General report
    def WriteReport(self):
        report = "Image name: '{}'\nImage extension: '{}'\nSpeck detected: {}\nStains detected: {}\nTime: {}\nStatus: '{}'\n\n".format(self.image_name, self.image_extension, self.number_speck, self.number_stains, self.time, self.status)
        return report
#TODO remove ext PNG becouse cv2 knows ext...
    def ImageReport(self, result_image):
        path = os.path.abspath(os.getcwd())
        if(self.status != "Dirty"):
            cv2.imwrite("{}/ImageResults/Clean/Report_{}.png".format(path, self.image_name), result_image)
        else:
            cv2.imwrite("{}/ImageResults/Dirty/Report_{}.png".format(path, self.image_name), result_image)