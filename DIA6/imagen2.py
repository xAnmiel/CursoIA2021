import cv2
import matplotlib.pyplot as plt



#print(img.shape)
#print(img.ndim)
#print(img.shape[0])

#img[:,:,0]=0
#img[:,:,0]=255
#img=cv2.imread('IMGS/p.png',cv2.IMREAD_GRAYSCALE)                #0 gris, 1 color, -1 canal alfa
img=cv2.imread('IMGS/p.png')   #",cv2.IMREAD_COLOR"             #color

#print(img)
print(img.shape)
#imgInv = img[:,:,::-1]
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#HSV (hue saturation value)
r,g,b=cv2.split(imgRGB)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(r, cmap = 'gray');plt.title('Canal Rojo');
plt.subplot(142);plt.imshow(g, cmap = 'gray');plt.title('Canal Verde');
plt.subplot(143);plt.imshow(b, cmap = 'gray');plt.title('Canal Azul');

img2 = cv2.merge((b,g,r))
plt.subplot(144);plt.imshow(img2[:,:,::-1],cmap='gray');plt.title('Imagen unida');
cv2.imwrite('img_copy.png',img2)


#plt.imshow(imgInv)                                             #imagen original
#plt.imshow(img,cmap='gray')
plt.waitforbuttonpress()
#cv2.imshow("Imagen",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
