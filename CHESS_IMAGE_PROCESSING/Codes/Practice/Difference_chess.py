import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('opencv_frame_0.png')
img1 = cv2.imread('opencv_frame_1.png')
rows,cols,ch = img1.shape

pts1 = np.float32([[124,60],[760,44],[116,693],[770,704]])
pts2 = np.float32([[0,0],[800,0],[0,800],[800,800]])
pts3 = np.float32([[125,50],[765,35],[113,683],[770,697]])
pts4 = np.float32([[0,0],[800,0],[0,800],[800,800]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(800,800))
M1 = cv2.getPerspectiveTransform(pts3,pts4)
dst1 = cv2.warpPerspective(img1,M1,(800,800))

#cv2.imwrite('opencv_frame_1_warp.png',dst1)
#cv2.imshow('a', cv2.imread('opencv_frame_1_warp.png'))
#plt.subplot(121),plt.imshow(img1),plt.title('Input')
#plt.subplot(122),plt.imshow(dst1),plt.title('Output')
#plt.show()

font = cv2.FONT_HERSHEY_SIMPLEX
row='1'
yc=750
y1=700
y2=800
arr=[]
arr1=[]
img_counter=0
for y in range(8):
    column='a'
    xc=50
    x1=0
    x2=100
    for x in range(8):
        cell=row+column
        cv2.putText(dst,cell,(xc,yc),font ,0.5 ,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(dst1,cell,(xc,yc),font ,0.5 ,(0,0,255),1,cv2.LINE_AA)
        crp=dst[y1:y2,x1:x2]
        crp1=dst1[y1:y2,x1:x2]
        #img_name = "opencv_frame_{}.png".format(img_counter)
        #cv2.imshow(img_name, crp)
        #img_counter += 1
        arr.append(crp)
        arr1.append(crp1)
        x1+=100
        x2+=100
        column=chr(ord(column)+1)
        xc+=100
    row=chr(ord(row)+1)
    yc-=100
    y1-=100
    y2-=100
    
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)

for i in arr:
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imshow(img_name, i)
    img_counter += 1
#img_counter = 0
#for i in arr1:
#    img_name1 = "opencv_frame1_{}.png".format(img_counter)
#    cv2.imshow(img_name1, i)
#    img_counter += 1
#print (img_counter)

if cv2.waitKey(0) & 0xff == 'q':
    cv2.destroyAllWindows()
