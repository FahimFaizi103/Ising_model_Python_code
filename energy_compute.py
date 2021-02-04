
def energy_compute(spin,J):
    import numpy as np
    
    sumOfNeighbors = np.roll(spin,1,axis = 1) + np.roll(spin,-1,axis = 1) + np.roll(spin,1,axis = 0) + np.roll(spin,-1,axis = 0)
    
    # each spin sigma_m contributes an energy Em to the total energy.
    Em = -J*spin*sumOfNeighbors
    
    E_total = 0.5*np.sum(Em)
    Emean = E_total/np.size(spin)
    
    return[Emean]
    
    
    
    
    

