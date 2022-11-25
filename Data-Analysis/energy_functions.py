import numpy as np

def KE(m, v):
    '''
    Function to return the kinetic energy for a body of mass m and velocity v
    '''
    KE = 0.5*m*v**2
    return KE

def GPE(m, h):
    '''
    Function to return the gravitational potential energy for a body of mass m and at height h
    '''
    g = 9.81
    GPE = m*g*h
    return GPE