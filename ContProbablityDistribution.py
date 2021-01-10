# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:56:55 2020

@author: student-minecraft
"""

import numpy as np
from scipy.stats import norm, beta
import matplotlib.pyplot as plt
#%%

loc = 0
scale  = 1
x_vals = np.linspace(-5, 5, 100)
print(x_vals)

#plt.plot(x_vals, norm.pdf(x_vals))

arr = np.array([50, 100, 1000, 10000])
samples = []

for i in range (len(arr)):
    #s= np.random.normal(size = arr[i])
    sample = np.random.normal(loc, scale, size = arr[i])
    
    plt.figure()
    
    plt.hist(sample, bins = 25, density = False)
    
    plt.plot(x_vals, norm.pdf(x_vals, loc , scale))

#%%
x_vals = np.linspace(0, 1, 100)
print (x_vals)
a = 1
b = 1

plt.plot(x_vals, beta.pdf(x_vals, a, b))

#a = 100
#b = 100
flips = 10 
arr = np.arange(0, flips+1)
print(arr)

plt.figure()

for i in range (len(arr)):
    plt.plot(x_vals, beta.pdf(x_vals, a + arr[i], b + (flips-arr[i])))
    
plt.figure()
plt.plot(x_vals, beta.pdf(x_vals, a + 1, b + (flips - 1)))
sample = np.random.beta(a + 1, b + (flips - 1), size = 1000)
plt.hist(sample, bins = 25, density = True)

plt.figure()
for i in range (len(arr)):
    plt.plot(x_vals, beta.pdf(x_vals, a + arr[i], b + (flips-arr[i])))
    samples = np.random.beta(a + arr[i], b+ (flips-arr[i]), size = 1000)
    plt.hist(samples, bins = 25, density = True)
