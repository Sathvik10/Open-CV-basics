# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:40:48 2019

@author: sathvik
"""
import numpy as np
import cv2
img=cv2.imread('C:\\Users\\sathvik\\Desktop\\opencv\\butterfly.jpeg',0)


cv2.imshow("image",img)
cv2.waitKey(0)

cv2.imwrite("new.jpeg",img)
cv2.destroyAllWindows()