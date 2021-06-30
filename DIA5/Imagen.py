import cv2
import matplotlib.pyplot as plt



#print(img.shape)
#print(img.ndim)
#print(img.shape[0])

#img[:,:,0]=0
#img[:,:,0]=255
#img=cv2.imread('IMGS/p.png',cv2.IMREAD_GRAYSCALE)                #0 gris, 1 color, -1 canal alfa
img=cv2.imread('IMGS/p.png',cv2.IMREAD_COLOR)                #color

#print(img)
print(img.shape)
imgInv = img[:,:,::-1]
r,g,b=cv2.split(imgInv)
#plt.imshow(r)


plt.imshow(imgInv)                                             #imagen original
#plt.imshow(img,cmap='gray')
plt.waitforbuttonpress()
#cv2.imshow("Imagen",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


