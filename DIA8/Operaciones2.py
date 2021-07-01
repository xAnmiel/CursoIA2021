import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('IMGS/LogoCocacola.png',cv2.COLOR_BGR2RGB) 

#imgRes = cv2.bitwise_and(imgrect,imgcir,mask=None)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(img, cmap='gray')


plt.waitforbuttonpress()
