import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

filename = 'Chess.png'
img = cv2.imread(filename)
cv2.imshow('img',img)

rows,cols,ch = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
pts1 = np.float32([[9,9],[490,9],[9,490],[490,490]])
pts2 = np.float32([[0,0],[800,0],[0,800],[800,800]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(dst,M,(800,800))


font = cv2.FONT_HERSHEY_SIMPLEX
row='1'
yc=750
y1=700
y2=800
arr=[]
img_counter=0
for y in range(8):
    column='a'
    xc=50
    x1=0
    x2=100
    for x in range(8):
        cell=row+column
        cv2.putText(dst,cell,(xc,yc),font ,0.5 ,(0,0,255),2,cv2.LINE_AA)
        crp=dst[y1:y2,x1:x2]
        #img_name = "opencv_frame_{}.png".format(img_counter)
        #cv2.imshow(img_name, crp)
        #img_counter += 1
        arr.append(crp)
        x1+=100
        x2+=100
        column=chr(ord(column)+1)
        xc+=100
    row=chr(ord(row)+1)
    yc-=100
    y1-=100
    y2-=100
cv2.imshow('dst',dst)
cv2.imshow('cell',arr[63])
for i in arr:
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imshow(img_name, i)
    img_counter += 1
print (img_counter)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
