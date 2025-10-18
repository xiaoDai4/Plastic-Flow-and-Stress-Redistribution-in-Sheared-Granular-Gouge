import numpy as np
import math
def calculate_nonaffine(c_former_, c_later_, neighbor_):
    '''
    The theory of this function refer to airticle
        'Spatial correlation and temporal evolution of plastic heterogeneity in sheared granular materials'

    Parameters
    ----------
    c_former_ : 
        Particle's coordinate in former step.
    c_later_ : 
        Particle's coordinate in later step.
    neighbor_ : 
        Particle's neighbors.

    Returns
    -------
    nonaffine_:
         A vector that store the nonaffine displacement.

    '''
    n_particles_ = c_former_.shape[0]
    nonaffine_ = np.zeros(n_particles_)
    for i_ in range(n_particles_):
        X_ = np.zeros([2, 2])
        Y_ = np.zeros([2, 2])
        if len(neighbor_[i_]) <= 2:  #  if the particle with no neighbor, just assign a 0 to the nonaffine
            nonaffine_[i_] = 0
            continue
        for j_ in neighbor_[i_]:
            # calculate X_
            X_ = X_ + np.tensordot((c_later_[j_] - c_later_[i_]), (c_former_[j_] - c_former_[i_]), axes=0)
            # calculate Y_
            Y_ = Y_ + np.tensordot((c_former_[j_] - c_former_[i_]), (c_former_[j_] - c_former_[i_]), axes=0)  
        # convert data type
        X_ = X_.astype('float64')
        Y_ = Y_.astype('float64')
        # calculate J_
        J_ = np.dot(X_,np.linalg.inv(Y_))
        # calculate nonaffine_
        for j_ in neighbor_[i_]:
            nonaffine_vector_ = c_later_[j_] - c_later_[i_] - np.dot(J_, c_former_[j_] - c_former_[i_])
            nonaffine_[i_] += nonaffine_vector_[0]**2 + nonaffine_vector_[1]**2
        nonaffine_[i_] /= len(neighbor_[i_])
    print('Calculate nonaffine displacement done')
    return nonaffine_



# nonaffine_ = calculate_nonaffine(c_former_, c_later_, neighbor_)