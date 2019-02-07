# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:02:20 2019

@author: Anuj Kumar
"""
#cutting a part of the image and pasting it somewhere else
import numpy as np
import cv2
image=cv2.imread('airplane.png')
print(image.shape)
roi=image[200:300,200:300]
image[400:500,400:500]=roi
image=cv2.imwrite('edited_plane.png',image)