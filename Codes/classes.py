import board
import digitalio
import smbus
from adafruit_motor import stepper
import PID.py

class inclinometre():
	def __init__(self, bus, adress):
		self.bus = bus
		self.adress = adress
	
	def lecture(self) :
		bear1 = self.bus.read_byte_data(self.address, 2)
        bear2 = self.bus.read_byte_data(self.address, 3)
        bear = (bear1 << 8) + bear2
        bear = bear/10.0
        return bear
		
class moteur():
	def __init__(self, coils, n_steps, delay):
		for coil in coils:
			coil.direction = digitalio.Direction.OUTPUT
		self.controleur = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
		self.n_steps = n_steps
		self.delay = delay
	
	# def spin(self, alpha) :
	# 	direction = stepper.FORWARD if alpha > 0 else stepper.BACKWARD
	# 	for step in range(int(alpha/360*self.n_steps)) :
	# 		self.controleur.onestep(direction = direction)
	# 		time.sleep(self.delay)

	def spinDual(moteurL, moteurR, stepL, stepR) :
		l, r = 0, 0
		dirL = stepper.FORWARD if stepL > 0 else stepper.BACKWARD
		dirR = stepper.FORWARD if stepR > 0 else stepper.BACKWARD
		stepL, stepR = abs(stepL), abs(stepR)
		while (l <= stepL) && (r <= stepR) :
			if r <= stepR :
				moteurR.controleur.onestep(direction = dirR)
			if l <= stepL :
				moteurR.controleur.onestep(direction = dirR)
			time.sleep(self.delay)

	def deg_to_steps(self, alpha) :
		return int(alpha/360*self.n_steps)

class segway():
	def __init__(self, moteurL, moteurR, inclinometre, timestep):
		self.moteurL = moteurL
		self.moteruR = moteruR
		self.inclinometre = inclinometre
		self.timestep = timestep
		self.PID = PID()
		segway.PID.setSampleTime(timestep)

	def stabilisation(self) :
		self.PID.update(self.inclinometre.lecture())
		self.moteurL.spin(self.PID.output)
		self.moteurR.spin(self.PID.output)




		