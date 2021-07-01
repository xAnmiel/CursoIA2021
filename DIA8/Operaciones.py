import cv2
import numpy as np
import matplotlib.pyplot as plt

imgrect=cv2.imread('IMGS/rectangulo.jpg',cv2.IMREAD_GRAYSCALE) 
imgcir=cv2.imread('IMGS/circulo.jpg',cv2.IMREAD_GRAYSCALE) 

imgRes = cv2.bitwise_and(imgrect,imgcir,mask=None)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(imgrect, cmap='gray')
plt.subplot(142);plt.imshow(imgcir,cmap='gray')
plt.subplot(143);plt.imshow(imgRes,cmap='gray')


print(imgrect.shape)

plt.waitforbuttonpress()