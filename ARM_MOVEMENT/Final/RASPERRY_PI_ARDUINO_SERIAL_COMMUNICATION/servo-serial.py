import serial
from time import sleep
ser = serial.Serial("/dev/ttyACM0",9600)
ser.flushInput() 

try:
        move="b8c61"
        ser.write(move.encode('ascii'))
        """sleep(30)]
        move="e7e51"
        ser.write(move.encode('ascii'))"""
        
except KeyboardInterrupt:
    ser.close()
