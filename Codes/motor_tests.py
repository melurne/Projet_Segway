import classes.py
import pinout.py

print("Initializing motors")
moteurL = moteur(coils = coilsL, n_steps = NSTEPS, delay = DELAY)
moteurR = moteur(coils = coilsR, n_steps = NSTEPS, delay = DELAY)

print("Spinning ...")
moteur.spinDual(moteurL, moteurR, 20, 0)
print("Finished.")