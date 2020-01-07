#pylint: disable=no-member
import RPi.GPIO as GPIO
from chili_pad.driver import Driver as CP

cp = CP()

GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
pwm = GPIO.PWM(12, 1)
pwm.start(50)

pass