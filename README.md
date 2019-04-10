# Chess Playing AI Bot
**Project done in Srishti 2019 (Annual Techno-Hobby Exhibition of IIT Roorkee)**

Note: This ReadMe is a work-in-progress.


## ABSTRACT
Chess Playing Bot is an Autonomous Bot which
* captures and processes the present state of the chessboard using Raspberry Pi 3 and Pi camera module,
* detects the chess piece on each square of chessboard using a trained Convolutional Neural Network (CNN), 
* predicts the best move for computer side using Stockfish chess engine and 
* executes the move using Arduino controlled Robotic Arm made up of servo motors and 3D printed parts.

## TABLE OF CONTENTS
- [Team Members](#team-members)
- [Pre-Requisites](#pre-requisites)
  - [Software](#software)
  - [Hardware](#hardware)
- [Working](#working)
- [Design](#design)
- [Applications](#applications)
- [Future Scope](#future-scope)

## <a name="team-members"></a>TEAM MEMBERS
1. [Rohit Jethani](https://github.com/rohitjethani)
2. [Himanshu Chaudhary](https://github.com/himanshuamd1)
3. [Harsh Patel](https://github.com/harshpatel097)
4. [Mayank Sharma](https://github.com/sharmamayank1741)

## <a name="pre-requisites"></a>PRE-REQUISITES
### <a name="software"></a>1. Software:
* Raspian
* Arduino IDE for Raspberry Pi (linux ARM)
* Python with opencv, numpy, matplotlib, tensorflow, chess
* Chess Engine-Stockfish (built from source for linux arm)
* Solidworks for Windows

### <a name="hardware"></a>2. Hardware:
* Raspberry Pi 3
* Arduino Uno/Mega
* Raspberry Pi Camera Module
* TowerPro MG995 servo motors - 3
* TowerPro MG90s servo motor
* TowerPro SG90 servo motor
* Small Breadboard

* 3D Printed Parts ([STL](STL%20files%20of%203D%20printed%20parts)/[SLDPRT](https://grabcad.com/library/chess-playing-bot-1 ))

## <a name="working"></a>WORKING
1) As soon as the code is run, the Pi camera shows a live video of the chess board after warping.

Resolution of video: 800 x 800 pixels.
For warping, we calculated the Transformation matrix by using matplotlib.pyplot as it gives the coordinates of all pixels. When the (x,y) coordinates of all the four corners are obtained, it can entered in pts1 in the following code:
```python
pts1 = np.float32([[490,62],[374,707],[106,332],[753,446]]) #this will change according to position and orientation of board
pts2 = np.float32([[0,0],[0,800],[800,0],[800,800]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(800,800))
```
2) Pressing the Spacebar captures the current state of the chessboard (800 x 800 RGB image), crops it into 64 smaller images (100 x 100) corresponding to individual squares of the board and saves them in a folder.

3) The trained CNN detects the piece in each of the 64 squares and a 8 x 8 array of the chess board is generated.

Piece recognition is classification problem of 13 classes.
- King, Queen, Bishop, Knight, Rook, Pawn each for Black and White
- Empty sqaure

4) This array is then converted to a [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) file.
5) The Chess library of Python is used to convert the FEN to board representation.
6) The board information is then given to Stockfish which gives the list of all legal moves along with their respective scores.
7) The best possible move is selected according to the score and is sent to Arduino via Serial Communication.
8) The Arduino code then processes the initial and final squares and accordingly gives the values of angles in degrees to the servo motors.
9) Finally the servos execute the command and the move is made.
10) After every move by the human side, steps 2 to 9 are repeated.

## <a name="design"></a> DESIGN:
The Standard Tournament Size Chessboard (17" x 17") is fixed on a Plywood (3ft x 3ft x 0.25").

The camera stand consists of
 * PVC pipe (120cm long and diameter 2.6cm)
 * PVC L shaped joint
 * 3D printed pipe-ply and pipe-camera joints


Instead of the conventional x-y coordinate system, we decided to try a different type of robotic arm called [SCARA](https://en.wikipedia.org/wiki/SCARA). SCARA was chosen as it is relatively easier to construct.
SCARA can be co-related with a human arm with two joints- shoulder and elbow which help in motion along in XY plane.
The Arm comprises of Aluminium Square Pipe (side=1.6cm, length=100cm), four servo motors (with attachments) and eighteen 3D printed parts.
The stepwise assembly of the robotic arm can be found in this [video].

## <a name="applications"></a>APPLICATIONS
1. It can be used by beginners for learning and practicing the game.
2. Instead of playing chess on a mobile or computer, we can play it using an actual chess set.

## <a name="future-scope"></a>FUTURE SCOPE
1. The accuracy and repeatability of robotic arm can be improved by using better (and costlier) servo motors, replacing them with stepper motors or using encoders.
2. The accuracy of piece detection greatly depends on the lighting conditions change. We can use floodlights to solve this. Also we can place the camera at a different place to capture the image from a different angle to improve accuracy.
3. The piece detection time can be reduced upto one-third of its current value by using grayscale images for training and testing the model.
4. Since we are generating a FEN file after every human move, our bot cannot detect illegal moves. This can be overcome by saving all the previous states of the board. We can save all the moves of a game in [PGN](https://en.wikipedia.org/wiki/Portable_Game_Notation) file.
