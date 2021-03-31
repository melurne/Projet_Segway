import classes.py
import pinout.py

moteurL = moteur(coils = coilsL, n_steps = NSTEPS, delay = DELAY)
moteurR = moteur(coils = coilsR, n_steps = NSTEPS, delay = DELAY)
inclinometre = inclinometre(smbus.SMBus(0), adress_inclinometre)

segway = segway(moteurL, moteurR, inclinometre, timestep, fault_IRQ)

segway.PID.setKp(P)
segway.PID.setKi(I)
segway.PID.setKd(D)
segway.PID.SetPoint = offset_inclinometre
