# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 23:11:33 2019

@author: sathvik
"""

import cv2
import numpy as np
img=cv2.imread('C:\\Users\\sathvik\\Desktop\\opencv\\butterfly.jpeg',0)

img=cv2.GaussianBlur(img,(5,5),0)
blur=np.hstack([cv2.Canny(img,0,70)])
cv2.imshow("image",blur)
cv2.waitKey(0)

cv2.imwrite("canny.jpeg",blur)
cv2.destroyAllWindows()