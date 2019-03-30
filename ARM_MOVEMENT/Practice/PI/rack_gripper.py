import RPi.GPIO as GPIO
from time import sleep

rack=29
gripper=31
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gripper, GPIO.OUT)
GPIO.setup(rack, GPIO.OUT)
pwm_rack=GPIO.PWM(rack, 50)
pwm_grip=GPIO.PWM(gripper, 50)
pwm_rack.start(2.5)
pwm_grip.start(2.5)

def SetAngle(angle,pin,pwm):
	duty = angle / 18 + 2.5
	GPIO.output(pin, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(pin, False)
	pwm.ChangeDutyCycle(0)

SetAngle(0,rack,pwm_rack) #up
#SetAngle(120,gripper,pwm_grip)
GPIO.output(gripper,True)
pwm_grip.ChangeDutyCycle(8.5) #open

sleep(1)
SetAngle(130,rack,pwm_rack) #down
sleep(1)

#SetAngle(180,gripper,pwm_grip)
#SetAngle(180,gripper,pwm_grip)
#SetAngle(180,gripper,pwm_grip)
pwm_grip.ChangeDutyCycle(10.5) #close
sleep(1)
SetAngle(0,rack,pwm_rack) #up
sleep(5)
SetAngle(130,rack,pwm_rack) #down
sleep(1)
#SetAngle(120,gripper,pwm_grip)
pwm_grip.ChangeDutyCycle(8.5) #open
sleep(1)
SetAngle(0,rack,pwm_rack) #up

pwm_grip.ChangeDutyCycle(0)
#pwm.stop()
GPIO.cleanup()
