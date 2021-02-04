def sample_spins_randomly(spin, J):
    
    import numpy as np

    row = np.random.randint(0,np.size(spin,0)) # produces a random integer between [0,size of rows). i.e. (1,101) produces number between 1 and 100.
    col = np.random.randint(0,np.size(spin,1))

    above = ( (row -1 )%(np.size(spin,0)) )
    below = ( (row +1 )%(np.size(spin,0)) )
    left  = ( (col -1 )%(np.size(spin,1)) )
    right = ( (col +1 )%(np.size(spin,1)) )

    neighbors = [spin[above,col], spin[row,left], spin[row,right], spin[below,col]]

    dE = 2*J*spin[row,col]*np.sum(neighbors)
    
    return[dE, row, col]



