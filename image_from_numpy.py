# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:24:30 2019

@author: Anuj Kumar
"""
#importing opencv
import cv2
#importing numpy
import numpy as np
#creating a numpy array
img=np.zeros((3,3),dtype=np.uint8)
#print(img)
#converting it to BGR format.
img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#print(img)
