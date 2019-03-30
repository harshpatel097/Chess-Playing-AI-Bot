import cv2
import numpy as np
from matplotlib import pyplot as plt
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (800, 800)
camera.framerate = 40
rawCapture = PiRGBArray(camera, size=(800, 800))
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    img = frame.array
    rows,cols,ch = img.shape

    pts1 = np.float32([[481,52],[360,702],[92,323],[740,441]])
    pts2 = np.float32([[800,0],[0,800],[0,0],[800,800]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(img,M,(800,800))

    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()

#cv2.imwrite('warped1.png', dst)
