def spin_flip_Met(dE, kT, spin, row, col):
    import numpy as np
    
    P = np.exp(-dE/kT)

    u = np.random.uniform(0,1)

    if u<= min(1,P):
            spin[row,col] = -spin[row,col]
    else:
            spin[row,col] =  spin[row,col]
            
    return[spin]
