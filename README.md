# Chess Playing AI Bot
**Project done in Srishti 2019 (Annual Techno-Hobby Exhibition of IIT Roorkee)**

Note: This ReadMe is a work-in-progress.


## ABSTRACT
Chess Playing Bot is an Autonomous Bot which
	captures and processes the present state of the chessboard using Raspberry Pi 3 and Pi camera module,
	detects the chess piece on each square of chessboard using a trained Convolutional Neural Network (CNN), 
	predicts the best move for computer side using Stockfish chess engine and 
	executes the move using Arduino controlled Robotic Arm made up of servo motors and 3D printed parts.

## [TEAM MEMBERS](#team-members)
# <a name="team-members"></a>Team Members
1. [Rohit Jethani](https://github.com/rohitjethani)
2. [Himanshu Chaudhary](https://github.com/himanshuamd1)
3. [Harsh Patel](https://github.com/harshpatel097)
4. Mayank Sharma

## PRE-REQUISITES
### 1. Software:
* Raspian
* Arduino IDE for Raspberry Pi (linux ARM)
* Python with opencv, numpy, matplotlib, tensorflow, chess
* Chess Engine-Stockfish (built from source for linux arm)
* Solidworks for Windows

### 2. Hardware:
* Raspberry Pi 3
* Arduino Uno/Mega
* Raspberry Pi Camera Module
* TowerPro MG995 servo motors - 3
* TowerPro MG90s servo motor
* TowerPro SG90 servo motor
* Small Breadboard

### 3. Design:
* Aluminium Square Pipe side=1.6cm, length=100cm
* Plywood 90cm x 90cm x 0.6cm
* PVC pipe 120cm long and diameter 2.6cm
* 3D printed parts ([SLDPRT](https://grabcad.com/library/chess-playing-bot-1) / [STL](STL%20files%20of%203D%20printed%20parts))

## WORKING
1) As soon as the code is run, the Pi camera shows a live video of the chess board after warping.
2) Pressing the Spacebar captures the current state of the chessboard, crops it into 64 smaller images and saves them.
3) The trained CNN detects the piece in each of the 64 squares and a 8 x 8 array of the chess board is generated.
4) This array is then converted to a FEN file.
5) The Chess library of Python is used to convert the FEN to board representation.
6) The board information is then given to Stockfish which gives the list of all legal moves along with their respective scores.
7) The best possible move is selected according to the score and is sent to Arduino via Serial Communication.
8) The Arduino code then processes the initial and final squares and accordingly gives the values of angles in degrees to the servo motors.
9) Finally the servos execute the command and the move is made.
10) After every move by the human side, steps 2 to 9 are repeated.

### Machine Learning
- The first step used is to capture the image of the chess board from the video stream of the PI camera connected at the top of the chess board through a clamp.
	Captured image (800x800x3)

- Then the captured image is subsequently cropped into 64 smaller images (each of the individual piece of the chess board)
	64 images each of dimension (100x100x3)

- Each of the 64 images is passed through a trained Convolutional Neural Network (CNN) to detect the piece it contains.
	- Classification problem of 13 classes
		- Each for black and white
			- King, Queen, Bishop, Knight, Rook, Pawn
		- Empty class
## APPLICATIONS
## FUTURE SCOPE
