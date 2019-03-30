import cv2
import numpy as np
cap=cv2.VideoCapture(1)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
img_counter = 0
cap.set(3,800)
cap.set(4,800)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rows,cols,ch = img.shape
    # cols-1 and rows-1 are the coordinate limits.
    M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    pts1 = np.float32([[9,9],[490,9],[9,490],[490,490]])
    pts2 = np.float32([[0,0],[800,0],[0,800],[800,800]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(dst,M,(800,800))

    cv2.imshow('frame',img)
    #cv2.imshow('dst',dst)
    #out.write(fram)
    k=cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, img)
        print("{} written!".format(img_name))
        img_counter += 1
cap.release()
#out.release()
cv2.destroyAllWindows()
