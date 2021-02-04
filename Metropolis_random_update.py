import numpy as np
from energy_compute import energy_compute
from sample_spins_randomly import sample_spins_randomly
from spin_flip_Met import spin_flip_Met
import time
import matplotlib.pyplot as plt
#%% Define simulation and model parameters

J = 1 # interaction strength 
kT = 2.27 # temperature
numSpinsPerDim = 4
probSpinUp = 0.5
numSweeps = 10**5
equilib_time = round(0.1*numSweeps)

#%%
# Declaring variables
Mmean = np.zeros(numSweeps)
Emean = np.zeros(numSweeps)

spin = np.sign(probSpinUp - np.random.rand(numSpinsPerDim, numSpinsPerDim) )
plt.pcolor(spin)
plt.show()

#%%

# Sample spins randomly.
t = time.time()

for SweepIndex in range(0,numSweeps,1):
    for i in range(0,np.size(spin),1):
        
        [dE, row, col] = sample_spins_randomly(spin, J)
        [spin] = spin_flip_Met(dE, kT, spin, row, col)

    Mmean[SweepIndex] = np.mean(spin)
    [Emean[SweepIndex]] = energy_compute(spin,J)

time_elapsed = time.time() - t
print(time_elapsed)