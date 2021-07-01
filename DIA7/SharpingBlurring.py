import cv2
import numpy as np

img=cv2.imread('IMGS/carro.jpg') 
cv2.imshow('imagen original', img)
cv2.waitKey()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen gray', imgGray)
cv2.waitKey()

#filtro = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
filtro = np.ones((3,3))/9
imgsharped = cv2.filter2D(imgGray,-1,kernel=filtro)
cv2.imshow('imagen sharped', imgsharped)
cv2.waitKey()

cv2.destroyAllWindows()