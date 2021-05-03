import board
import digitalio
import smbus
from adafruit_motor import stepper
import PID.py
import RPi.GPIO as GPIO

GPIO_edge = {"r": GPIO.RISING, "f": GPIO.FALLING}

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
	delay = DELAY
	def __init__(self, coils, n_steps, delay):
		for coil in coils:
			coil.direction = digitalio.Direction.OUTPUT
		self.controleur = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
		self.n_steps = n_steps
#		self.delay = delay

	@staticmethod
	def spinDual(moteurL, moteurR, stepL, stepR) :
		l, r = 0, 0
		dirL = stepper.FORWARD if stepL > 0 else stepper.BACKWARD
		dirR = stepper.FORWARD if stepR > 0 else stepper.BACKWARD
		stepL, stepR = abs(stepL), abs(stepR)
		while (l <= stepL) and (r <= stepR) :
			if r <= stepR :
				moteurR.controleur.onestep(direction = dirR)
			if l <= stepL :
				moteurR.controleur.onestep(direction = dirR)
			time.sleep(moteur.delay)

	def deg_to_steps(self, alpha) :
		return int(alpha/360*self.n_steps)

class security_exception(Exception):
    def __init__(self, message="Surtension du controler\n"):
        self.message = message
        super().__init__(self.message)

class security_checks():
    def __init__(self, pin, edgeType, exceptionMessage):
        self.pin = pin
        self.exceptionMessage = exceptionMessage
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, edgeType, callback = self.exception_handler, bouncetime=50)

    def exception_handler(self):
        GPIO.cleanup()
        raise security_exception(self.exceptionMessage)

class segway():
	def __init__(self, moteurL, moteurR, inclinometre, timestep, safety):
		self.moteurL = moteurL
		self.moteruR = moteruR
		self.inclinometre = inclinometre
		self.timestep = timestep
		self.PID = PID()
		segway.PID.setSampleTime(timestep)
		self.safeties = [security_checks(test[0], GPIO_edge[test[1]], test[2]) for test in safety]

#	def stabilisation(self):
#		self.PID.update(self.inclinometre.lecture())
#		moteur.spinDual(    self.moteurL,
#							self.moteurR,
#							moteurL.deg_to_steps(self.PID.output),
#							moteurR.deg_to_steps(self.PID.output))
