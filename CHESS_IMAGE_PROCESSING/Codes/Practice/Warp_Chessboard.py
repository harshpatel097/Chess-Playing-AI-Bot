import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('chess2.png')
rows,cols,ch = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),0,1)
dst = cv2.warpAffine(img,M,(cols,rows))
pts1 = np.float32([[30,440],[762,405],[378,56],[412,789]])
pts2 = np.float32([[0,0],[800,800],[800,0],[0,800]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(dst,M,(800,800))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv2.imwrite('chess2_warp.png', dst)
