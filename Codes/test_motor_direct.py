from pinout import *
import board
import digitalio
import smbus
from adafruit_motor import stepper
import RPi.GPIO as GPIO
import time

#coils = (22, 27, 4, 17)
#for coil in coils:
 #   GPIO.setup(coil, GPIO.OUT)
coils = 	(
			digitalio.DigitalInOut(board.D22), #A1
			digitalio.DigitalInOut(board.D27), #A2
			digitalio.DigitalInOut(board.D4), #B1
			digitalio.DigitalInOut(board.D17), #B2
			)
for coil in coils:
            coil.direction = digitalio.Direction.OUTPUT
controleur = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)


sequence = ((1, 0, 0, 1), (1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1))


while True:
    time.sleep(0.001)
    controleur.onestep(direction = stepper.FORWARD)
    """for i in range(4):
        GPIO.output(coils[0], sequence[i][0])
        GPIO.output(coils[1], sequence[i][1])
        GPIO.output(coils[2], sequence[i][2])
        GPIO.output(coils[3], sequence[i][3])
        time.sleep(0.001)"""
        