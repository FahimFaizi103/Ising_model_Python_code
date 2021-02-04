import numpy as np
import matplotlib.pyplot as plt

#%% Trace plot of magnetisation per spin
plt.figure()
plt.plot(Mmean)
plt.ylabel('Magnetisation density')
plt.xlabel('MC Steps')
plt.show 
#%% Trace plot of energy density
plt.figure()
plt.plot(Emean)
plt.ylabel('Energy density')
plt.xlabel('MC Steps')
plt.show 
#%% Histogram of spin
plt.figure()
plt.hist(Mmean[equilib_time:], bins = 'auto');
plt.xlabel('spin values')
plt.title('Historam of spins')
#%% Free energy profile
Num_bins = 17;
[values, edges] = np.histogram(Mmean[equilib_time:], bins = Num_bins)
values = values/sum(values);
plt.plot(edges[1:len(edges)],-np.log(values)-np.min(-np.log(values)))
#%% Autocorrelation function
def autocorr(x):
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = np.correlate(x, x, mode = 'full')[-n:]
    assert np.allclose(r, np.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
    result = r/(variance*(np.arange(n, 0, -1)))
    return result
#%% Autocororelation for magnetisation
corr = autocorr(Mmean[equilib_time:])
plt.plot(corr)
plt.xlim([0,2000])
#%% Autocorrelatio for energy
corr = autocorr(Emean[equilib_time:])
plt.plot(corr)
plt.xlim([0,2000])



