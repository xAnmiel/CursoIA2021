import cv2

img=cv2.imread('IMGS/p.png')
print(img.shape)
print(img.ndim)
print(img.shape[0])

img[:,:,0]=0
#img[:,:,0]=255


cv2.imshow("pinguino",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


