# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:12:45 2019

@author: Anuj Kumar
"""
#using opencv to apply border of 15 px to the image.
import numpy as np
import cv2
image=cv2.imread('boat.png')
print(image.shape)
s=image.shape
#assuming the image is square
for i in range(0,s[0]):
    #adding a border of 15 px
    for j in range (0,15):
        image[i,j]=[0,0,0]
        image[j,i]=[0,0,0]
        image[i,j+(s[0]-15)]=[0,0,0]
        image[j+(s[0]-15),i]=[0,0,0]
image=cv2.imwrite('edited_boat.png',image);
print("Done")