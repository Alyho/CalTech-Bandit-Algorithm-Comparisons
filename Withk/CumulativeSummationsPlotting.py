# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:16:12 2020

@author: student-minecraft
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as io

def csum (d, array, is2Darr):
    if (is2Darr == "true"): 
        for e in range(0, len(array)):
            for f in range (0, len(array)):
                d[e][f] = array[e][f] + d[e][f-1]
    else:
        for i in range (0, len(a)):
            d[i] = array[i] + d[i-1] 
            
    return d

#%%
a = np.array([0, 0, 1, 1, 2, 5, 10, 0, 0, 1])
b = np.zeros(len(a))
Sum = 0
    
print(csum(b, a, "false"))

b = np.cumsum(a)
print(b)

c = np.array((np.random.choice(3, 3), np.random.choice(3, 3), np.random.choice(3, 3)))
print(c)

#%%

arr = np.zeros((len(c), len(c)))
    
print(csum(arr, c, "true"))

d = np.cumsum(c, axis=1)
print(d)

#%%

k=20
repetition = 100
trials = 20000

upperBound = io.loadmat("kUpperBound" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")

big_array = upperBound["big_array_ucb"]

cumsum = np.cumsum(big_array, axis = 0)

mean = np.empty(trials)
stdev = np.empty(trials)
for g in range (trials):
    mean[g] = np.mean(cumsum[g])
    stdev[g] = np.std(cumsum[g])
    
#%%
plt.figure()
plt.plot(np.arange(1, trials + 1), mean, color = 'blue')
plt.fill_between(np.arange(1, trials + 1), mean -   
	stdev, mean + stdev, alpha = 0.1, color = 'blue')
plt.xlabel('Trials')
plt.ylabel('Total Heads')
plt.title('Comparing')

    

