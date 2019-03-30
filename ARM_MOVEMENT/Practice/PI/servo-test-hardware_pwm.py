from time import sleep
import pigpio
import RPi.GPIO as GPIO

elbow=18
shoulder=13
rack=29
gripper=31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(rack,GPIO.OUT)
GPIO.setup(gripper, GPIO.OUT)
pwm_rack=GPIO.PWM(rack,50)
pwm_grip=GPIO.PWM(gripper, 50)

def SetAngle(angle,pin,pwm):
	duty = angle / 18 + 2.5
	GPIO.output(pin, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(pin, False)
	pwm.ChangeDutyCycle(0)

pwm_freq=50
elbow_default=95000
shoulder_default=50000
shoulder_final=88000
elbow_final=78000
shoulder_final2=92500
elbow_final2=79000
elbow_total=elbow_default+elbow_final-1000
shoulder_total=shoulder_default+shoulder_final-1000
pi = pigpio.pi()

pi.hardware_PWM(shoulder, 50, shoulder_default)
sleep(2)
pi.hardware_PWM(elbow, 50, elbow_default)
sleep(2)

for i in range(shoulder_default,shoulder_final,500):
    pi.hardware_PWM(shoulder, pwm_freq,i)
    sleep(0.02)

sleep(2)
for i in range(elbow_final,elbow_default,500):
   pi.hardware_PWM(elbow, pwm_freq, elbow_total-i)
   sleep(0.02)
sleep(2)

pwm_rack.start(2.5)
pwm_grip.start(2.5)

SetAngle(0,rack,pwm_rack) #up
GPIO.output(gripper,True)
pwm_grip.ChangeDutyCycle(8.5)
#pi.set_servo_pulsewidth(6, 1500) #open
sleep(1)
SetAngle(70,rack,pwm_rack) #down
sleep(1)
pwm_grip.ChangeDutyCycle(10.5)
#pi.set_servo_pulsewidth(6, 2200) #close
sleep(1)
SetAngle(0,rack,pwm_rack) #up
sleep(1)

for i in range(shoulder_default,shoulder_final,500):
    pi.hardware_PWM(shoulder, pwm_freq,shoulder_total-i)
    sleep(0.02)
    
sleep(1)

for i in range(elbow_final,elbow_default,500):
   pi.hardware_PWM(elbow, pwm_freq,i)
   sleep(0.02)
sleep(1)

SetAngle(70,rack,pwm_rack) #down
sleep(1)
pwm_grip.ChangeDutyCycle(8.5) 
#pi.set_servo_pulsewidth(6, 1500) #open
sleep(1)
SetAngle(0,rack,pwm_rack) #up
sleep(1)
pwm_grip.ChangeDutyCycle(0)
pwm_grip.stop()
