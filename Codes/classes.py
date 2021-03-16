import time
import board
import digitalio
from adafruit_motor import stepper

class inclinometre():
	def __init__(self, pin_i2c_data, pin_i2c_clk):
		self.pin_i2c_data = pin_i2c_data
		self.pin_i2c_clk = pin_i2c_clk
	
	def lecture(self) :
		pass	
		
class moteur():
	def __init__(self, coils, n_steps, delay):
		for coil in coils:
			coil.direction = digitalio.Direction.OUTPUT
		self.controleur = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
		self.n_steps = n_steps
		self.delay = delay
	
	def spin(self, alpha) :
		direction = stepper.FORWARD if alpha > 0 else stepper.BACKWARD
		for step in range(int(alpha/360*self.n_steps)) :
			self.controleur.onestep(direction = direction)
			time.sleep(self.delay)

class segway():
	def __init__(self, moteurL, moteurR, inclinometre):
		self.moteurL = moteurL
		self.moteruR = moteruR
		self.inclinometre = inclinometre

		