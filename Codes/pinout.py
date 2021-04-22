import board
import digitalio

coilsL = 	(
			digitalio.DigitalInOut(board.D22), #A1
			digitalio.DigitalInOut(board.D27), #A2
			digitalio.DigitalInOut(board.D4), #B1
			digitalio.DigitalInOut(board.D17), #B2
			)

coilsR = 	(
			digitalio.DigitalInOut(board.D26), #A1
			digitalio.DigitalInOut(board.D13), #A2
			digitalio.DigitalInOut(board.D5), #B1
			digitalio.DigitalInOut(board.D6), #B2
			)

fault_IRQ = [(18, "r", "Sur tension des moteurs")]

NSTEPS = 200
DELAY = 0.01
timestep = 0.1

P = 0.2
I = 0
D = 0

adress_inclinometre = 0x00
offset_inclinometre = 0
