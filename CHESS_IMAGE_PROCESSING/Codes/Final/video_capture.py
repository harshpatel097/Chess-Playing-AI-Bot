# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from subprocess import call
import os
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (800, 800)
camera.framerate = 40
rawCapture = PiRGBArray(camera, size=(800, 800))
image_counter=0
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    img = frame.array
    # show the frame
    rows,cols,ch = img.shape
# cols-1 and rows-1 are the coordinate limits.
    M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),0,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    pts1 = np.float32([[490,62],[374,707],[106,332],[753,446]]) #without border
    pts2 = np.float32([[800,0],[0,800],[0,0],[800,800]])
    #pts1 = np.float32([[30,440],[762,405],[378,59],[412,789]]) #with border
    #pts2 = np.float32([[800,0],[0,800],[0,0],[800,800]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(dst,M,(800,800))
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("img",img)
    cv2.imshow("dst", dst)
    #cv2.imwrite("img.jpg", img)
    k = cv2.waitKey(1) 
	
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
     
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_counter=0
        y1=700
        y2=800
        arr=[]
        img_counter=1
        for y in range(8):
            x1=0
            x2=100
            for x in range(8):
                crp=dst[y1:y2,x1:x2]
                #img_name = "opencv_frame_{}.png".format(img_counter)
        #       cv2.imshow(img_name, crp)
                #img_counter += 1
                arr.append(crp)
                x1+=100
                x2+=100
            y1-=100
            y2-=100
        for i in arr:
            img_name = "opencv_frame1_{}.jpg".format(img_counter)
            path='/home/pi/Desktop/New'
            cv2.imwrite(os.path.join(path , img_name), i)
            img_counter += 1
        #call("/usr/bin/expect -d /home/pi/final.exp", shell=True)

        
        
cv2.destroyAllWindows()
