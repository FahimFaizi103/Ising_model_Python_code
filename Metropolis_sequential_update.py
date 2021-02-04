import numpy as np
from energy_compute import energy_compute
import time
#%%
J = 1
kT = 2.0
numSim = 1
numSpinsPerDim = 4
probSpinUp = 0.5
numSweeps = 10**4
equilib_time = round(0.1*numSweeps)
#%%
# Declaring variables
Mmean = np.zeros(numSweeps)
Emean = np.zeros(numSweeps)

spin = np.sign(probSpinUp - np.random.rand(numSpinsPerDim, numSpinsPerDim) )

#%%

# Sample spins sequentially.
t = time.time()

for SweepIndex in range(0,numSweeps,1):
    for row in range(0,numSpinsPerDim,1):
        for col in range(0,numSpinsPerDim,1):


            above = ( (row -1 )%(np.size(spin,0)) )
            below = ( (row +1 )%(np.size(spin,0)) )
            left  = ( (col -1 )%(np.size(spin,1)) )
            right = ( (col +1 )%(np.size(spin,1)) )

            neighbors = [spin[above,col], spin[row,left], spin[row,right], spin[below,col]]

            dE = 2*J*spin[row,col]*np.sum(neighbors)

            P = np.exp(-dE/kT)

            u = np.random.uniform(0,1)

            if u<= min(1,P):
                spin[row,col] = -spin[row,col]
            else:
                spin[row,col] =  spin[row,col]

    Mmean[SweepIndex] = np.mean(spin)
    [Emean[SweepIndex]] = energy_compute(spin,J)

time_elapsed = time.time() - t
print(time_elapsed)
