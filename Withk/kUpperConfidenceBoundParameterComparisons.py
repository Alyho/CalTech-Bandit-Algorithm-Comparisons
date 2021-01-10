# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:25:01 2020

@author: student-minecraft
"""

import matplotlib.pyplot as plt
import scipy.io as io
import numpy as np

#%%

k = 20
repetition = 100
trials = 2000
a = [0.08, 0.09, 0.1, 0.2, 0.5, 2, 5, 10]

mean = np.empty(len(a))
stdev = np.empty(len(a))

for j in range (len(a)):
    upperBound = io.loadmat("kUpperBound" + str(k) + "_" + str(repetition) + "_" + str(trials) + "_" + str(a[j]) + "_" +  "Data.mat")

    mean[j] = upperBound["mean_max"][0][0] 
    
    stdev = upperBound["mean_max"][0][0] 

xvalues = np.arange(len(mean))

plt.figure()

plt.errorbar(xvalues, mean, 
             yerr = stdev,
             fmt='-o', ecolor='orangered', capsize=2)

plt.xlabel('Hyperparameter')
plt.ylabel('Total Heads')
plt.title('Comparing')
plt.xticks(xvalues, [a])

