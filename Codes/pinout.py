coilsL = 	(
			digitalio.DigitalInOut(board.D19), #A1
			digitalio.DigitalInOut(board.D26), #A2
			digitalio.DigitalInOut(board.D20), #B1
			digitalio.DigitalInOut(board.D21), #B2
			)

coilsR = 	(
			digitalio.DigitalInOut(board.D19), #A1
			digitalio.DigitalInOut(board.D26), #A2
			digitalio.DigitalInOut(board.D20), #B1
			digitalio.DigitalInOut(board.D21), #B2
			)

NSTEPS = 200
DELAY = 0.01
timestep = 0.1

P = 0.2
I = 0
D = 0

adress_inclinometre = 0x00
offset_inclinometre = 0