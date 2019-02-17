# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:44:36 2019

@author: sathvik
"""

import cv2
import numpy as np
img=cv2.imread('C:\\Users\\sathvik\\Desktop\\opencv\\butterfly.jpeg',1)

img=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("image",img)
cv2.waitKey(0)

cv2.imwrite("GaussianBlur.jpeg",img)
cv2.destroyAllWindows()
