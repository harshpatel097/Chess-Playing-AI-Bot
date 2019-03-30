from time import sleep
import pigpio
from array import *
shoulder_angle=[[0,0,0,0,57000,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,92500]]
elbow_angle=[[0,0,0,0,91000,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,79000]]
s_f1=0
s_f2=0
e_f1=0
e_f2=0
e_d=85000
s_d=50000
pi=pigpio.pi()
elbow=18
shoulder=13
freq=50

def arm_movement_empty(s_f1,e_f1,s_f2,e_f2):

    pi.hardware_PWM(shoulder,50,s_d)
    sleep(2)
    pi.hardware_PWM(elbow,50,e_d)
    sleep(2)

    if s_d<s_f1:
       for i in range(s_d,s_f1,500):
           pi.hardware_PWM(shoulder,freq,i)
           sleep(0.02)
    else:
        s_t=s_d+s_f1-1000
        for i in range(s_f1,s_d,500):
           pi.hardware_PWM(shoulder,freq,s_t-i)
           sleep(0.02)
    
    sleep(2)
    if e_d<e_f1:
       for i in range(e_d,e_f1,500):
           pi.hardware_PWM(elbow,freq,i)
           sleep(0.02)
    else:
        e_t=e_d+e_f1-1000
        for i in range(e_f1,e_d,500):
           pi.hardware_PWM(elbow,freq,e_t-i)
           sleep(0.02)
    sleep(10)
    if s_f1<s_f2:
       for i in range(s_f1,s_f2,500):
           pi.hardware_PWM(shoulder,freq,i)
           sleep(0.02)
    else:
        s_t=s_f1+s_f2-1000
        for i in range(s_f2,s_f1,500):
           pi.hardware_PWM(shoulder,freq,s_t-i)
           sleep(0.02)
    sleep(2)
    if e_f1<e_f2:
       for i in range(e_f1,e_f2,500):
           pi.hardware_PWM(elbow,freq,i)
           sleep(0.02)
    else:
        e_t=e_f1+e_f2-1000
        for i in range(e_f2,e_f1,500):
           pi.hardware_PWM(elbow,freq,e_t-i)
           sleep(0.02)    
    sleep(10)
    if e_f2<e_d:
       for i in range(e_f2,e_d,500):
           pi.hardware_PWM(elbow,freq,i)
           sleep(0.02)
    else:
        e_t=e_f2+e_d-1000
        for i in range(e_d,e_f2,500):
           pi.hardware_PWM(elbow,freq,e_t-i)
           sleep(0.02)
    sleep(2)
    if s_f2<s_d:
       for i in range(s_f2,s_d,500):
           pi.hardware_PWM(shoulder,freq,i)
           sleep(0.02)
    else:
        s_t=s_f2+s_d-1000
        for i in range(s_d,s_f2,500):
           pi.hardware_PWM(shoulder,freq,s_t-i)
           sleep(0.02)
           
def arm_movement_capture(s_f1,e_f1,s_f2,e_f2):
    pi.hardware_PWM(shoulder,50,s_d)
    sleep(2)
    pi.hardware_PWM(elbow,50,e_d)
    sleep(2)

    if s_d<s_f2:
       for i in range(s_d,s_f2,500):
           pi.hardware_PWM(shoulder,freq,i)
           sleep(0.02)
    else:
        s_t=s_d+s_f2-1000
        for i in range(s_f2,s_d,500):
           pi.hardware_PWM(shoulder,freq,s_t-i)
           sleep(0.02)
    
    sleep(2)
    if e_d<e_f2:
       for i in range(e_d,e_f2,500):
           pi.hardware_PWM(elbow,freq,i)
           sleep(0.02)
    else:
        e_t=e_d+e_f2-1000
        for i in range(e_f2,e_d,500):
           pi.hardware_PWM(elbow,freq,e_t-i)
           sleep(0.02)
    sleep(10)
    
    if e_f2<e_d:
       for i in range(e_f2,e_d,500):
           pi.hardware_PWM(elbow,freq,i)
           sleep(0.02)
    else:
        e_t=e_f2+e_d-1000
        for i in range(e_d,e_f2,500):
           pi.hardware_PWM(elbow,freq,e_t-i)
           sleep(0.02)
    sleep(2)
    if s_f2<s_d:
       for i in range(s_f2,s_d,500):
           pi.hardware_PWM(shoulder,freq,i)
           sleep(0.02)
    else:
        s_t=s_f2+s_d-1000
        for i in range(s_d,s_f2,500):
           pi.hardware_PWM(shoulder,freq,s_t-i)
           sleep(0.02)
    sleep(10)
    arm_movement_empty(s_f1,e_f1,s_f2,e_f2)
    
def arm_movement(move,empty):
    cells=[move[i:i+2] for i in range(0, len(move), 2)]
    switcher={
                'a':0,
                'b':1,
                'c':2,
                'd':3,
                'e':4,
                'f':5,
                'g':6,
                'h':7
                }
    i1=switcher.get(cells[0][0],-1)
    i2=switcher.get(cells[1][0],-1)
    j1=int(cells[0][1])-1
    j2=int(cells[1][1])-1
    s_f1=shoulder_angle[i1][j1]
    e_f1=elbow_angle[i1][j1]
    s_f2=shoulder_angle[i2][j2]
    e_f2=elbow_angle[i2][j2]
    if empty==1:
        arm_movement_empty(s_f1,e_f1,s_f2,e_f2)
    else:
        arm_movement_capture(s_f1,e_f1,s_f2,e_f2)
    
move='a5h8'
arm_movement(move,1) 
