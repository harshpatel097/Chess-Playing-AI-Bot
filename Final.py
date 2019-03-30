# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from subprocess import call
import os
import chess
import chess.uci
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
    img = frame.array
    # show the frame
    rows,cols,ch = img.shape
# cols-1 and rows-1 are the coordinate limits.
    M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),0,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    pts1 = np.float32([[481,52],[360,702],[92,323],[740,441]])
    pts2 = np.float32([[800,0],[0,800],[0,0],[800,800]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(dst,M,(800,800))
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img", img)
    cv2.imshow("dst", dst)
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

        call("/usr/bin/expect -d /home/pi/final.exp", shell=True)
        print("done")

        time.sleep(30)
#Let's try our code with the starting position of chess:
        file = open(r"fen.txt","r")
        fen = file.readline()
        #'rnbqkbnr/ppp1pppp/8/3P4/8/8/PPPP1PPP/RNBQKBNR b - - 0 0'
        file.close()
        board = chess.Board(fen)
        print(board)
        handler = chess.uci.InfoHandler()
#Now make sure you give the correct location for your stockfish engine file
#...in the line that follows: e.g., /home/.../stockfish_6_x64
        engine = chess.uci.popen_engine('/home/pi/Stockfish/src/stockfish')
        engine.info_handlers.append(handler)
        engine.position(board)
        if board.turn: print ('White to move')
        else: print ('black to move')
        m = -100
        bestmove = ''
        print(board.legal_moves.count())
        for el in board.legal_moves:
            engine.go(searchmoves=[el],movetime=500)
    #print (str(el), 'eval = ', round(handler.info["score"][1].cp/100.0,2))
            if round(handler.info["score"][1].cp/100.0,2) > m :
                m = round(handler.info["score"][1].cp/100.0,2)
                bestmove = el
        
        board.push(bestmove)
        print(board)
        print('\n the bestmove is : ',str(bestmove),'eval = ' ,  m)
        
cv2.destroyAllWindows()
