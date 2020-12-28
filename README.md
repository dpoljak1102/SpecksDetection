## Table of contents
* [General info](#general-info)
* [Setup](#setup)

## General info
This project is digital image processing in the programming language Python.
Since image processing covers a wide, diverse field, the aim of this project is to
implement an algoritham that will detect dust and dirt in optical engine.
The work was done
in collaboration with the company Orqa.

## Setup
To run this project, install:

```
import os
from skimage import data
import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy import ndimage
from skimage import measure
```
It’s best to run all the scripts and see what’s missing.

## How to use?

If you don’t want to run the scripts, you can just look at some results in the folder
SomeResults

Run scripts :
1. MASTER_speck_stains
2. MASTER_report
3. MASTER_image_analysis (setup your path "image_path" to your images)

When you run it check folder ImageResults, Speck, (Clean/Dirty)

In the TestImages folder there are a couple of dirty and clean pictures that you can try, if you want more pictures contact me
denis_poljak@hotmail.com

