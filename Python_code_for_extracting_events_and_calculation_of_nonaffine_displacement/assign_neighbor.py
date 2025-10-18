def assign_neighbor(distance_, threshold_):
    '''
    Parameters:
        distance_: distance matrix

    Returns
    -------
    neighbor_: list to store the neighbor of each particle

    '''
    n_particles_ = distance_.shape[0] 
    neighbor_ = [ [] for i_ in range(n_particles_) ] # list to store the neighbor of each particle
    for i_ in range(n_particles_):
        for j_ in range(n_particles_):
            if distance_[i_, j_] < threshold_:
                neighbor_[i_].append(j_)
    print('\nAssign neighbor done\n')
    return neighbor_
    
# neighbor_ = assign_neighbor(distance_, 3e-5)