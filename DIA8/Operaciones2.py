import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('IMGS/LogoCocaCola.png',cv2.COLOR_BGR2RGB) 
imGray= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
_,imgMask = cv2.threshold(imGray,127,255,cv2.THRESH_BINARY)
#imgRes = cv2.bitwise_and(imgrect,imgcir,mask=None)

imgresult = cv2.bitwise_not(imgMask)
img2 = cv2.bitwise_and(img,img,mask=imgresult)

img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(img)
plt.subplot(142);plt.imshow(imgMask, cmap='gray')
plt.subplot(143);plt.imshow(imgresult, cmap='gray')
plt.subplot(144);plt.imshow(img2)

plt.waitforbuttonpress()
