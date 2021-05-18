from classes import *
from pinout import *

print("Initializing motors")
moteurL = moteur(coils = coilsL, n_steps = NSTEPS, delay = DELAY)
moteurR = moteur(coils = coilsR, n_steps = NSTEPS, delay = DELAY)

print("Spinning ...")
moteur.spinDual(moteurL, moteurR, -400, -400)
print("Finished.")
