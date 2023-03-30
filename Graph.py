import cv2 as cv
import numpy as np

'''
img = cv.imread('cat.jpg')
img[100:200,100:200] = [0,0,255]
img[500:600,500:600] = img[1000:1100,1000:1100]
'''
img1=cv.resize(cv.imread('cat.jpg'),None,fx=0.45,fy=0.45,interpolation= cv.INTER_LINEAR)
img2=cv.resize(cv.imread('cat2.jpg'),None,fx=0.1,fy=0.1,interpolation= cv.INTER_LINEAR)
'''imgall = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('catt',imgall)'''
row,col,channel = img2.shape
roi = img1[0:row,0:col]

cv.imshow('ca',cv.add(img1,img2))
cv.waitKey(0)
cv.destroyAllWindows()
