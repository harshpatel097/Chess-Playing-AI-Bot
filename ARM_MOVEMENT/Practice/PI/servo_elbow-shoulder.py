import RPi.GPIO as GPIO
from time import sleep

shoulder=12
elbow=33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(elbow, GPIO.OUT)
GPIO.setup(shoulder, GPIO.OUT)
pwm_shoulder=GPIO.PWM(shoulder, 50)
pwm_elbow=GPIO.PWM(elbow, 50)
pwm_shoulder.start(2.5)
pwm_elbow.start(5)

def SetAngle(angle,pin,pwm):
	duty = angle / 18 + 2
	GPIO.output(pin, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	#GPIO.output(pin, False)
	#pwm.ChangeDutyCycle(0)

SetAngle(90,shoulder,pwm_shoulder)
sleep(2)
SetAngle(115,elbow,pwm_elbow)
#pwm.stop()
#GPIO.cleanup()
