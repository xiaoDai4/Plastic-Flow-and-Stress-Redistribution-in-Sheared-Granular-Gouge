import numpy as np
import math

def calculate_distance(c_):
    '''
    

    Parameters: 
    c_former_, c_later_ the former and later particles' information
    ----------
    def calculate_distance_ : TYPE
        DESCRIPTION:
            calculate the distance between particles

    Returns
    -------
    distance_: a matrix that store the distance between particles

    '''
    n_particles_ = c_.shape[0]  # the number of particles
    distance_ = np.zeros([n_particles_, n_particles_]) # matrix to store distance
    for i_ in range(n_particles_): # calculate distance
        for j_ in range(i_):
            distance_[i_, j_] = math.sqrt((c_[i_, 0] - c_[j_, 0])**2 + (c_[i_, 1] - c_[j_, 1])**2)
    for i_ in range(n_particles_): # diagonal matrix assignment
        for j_ in range(i_):
            distance_[j_, i_] = distance_[i_, j_]
    print('\nDistance calculation done\n')    
    
    return distance_