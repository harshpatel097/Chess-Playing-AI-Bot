from time import sleep
import pigpio

elbow=18
shoulder=13
pwm_freq=50
elbow_default=90000
shoulder_default=70000
shoulder_final=88500
elbow_final=78400
elbow_total=elbow_default+elbow_final-1000
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
