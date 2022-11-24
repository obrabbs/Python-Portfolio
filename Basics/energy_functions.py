import numpy as np

def kinetic_energy(m, v):
    KE = 0.5*m*v**2
    return KE

def gravitational_potential_energy(m, h):
    g = 9.81
    GPE = m*g*h
    return GPE