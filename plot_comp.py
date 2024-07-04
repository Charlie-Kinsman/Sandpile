import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import random as r
import math

with open('f.npy', 'rb') as f:
    a = np.load(f)

ind = a[:,0]
freq = a[:,1]
plt.plot(ind,freq)
plt.show()
plt.hist(freq,bins=15)
plt.show()
freq=np.log(freq)
n, bins, patches = plt.hist(freq,bins=15)
plt.show()

