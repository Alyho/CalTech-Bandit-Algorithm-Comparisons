# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:58:18 2020

@author: student-minecraft
"""

import numpy as np
import Coin_Environment as ce
import matplotlib.pyplot as plt
import scipy.io as io
#Epsilon greedy
#has to find success rate
#array of just sum and number of times

#for loop generates random number
#find mean of all the random numbers without storing them all
#every loop store sum and times

pheads = np.array([0.52,0.5,0.55,0.47])
coin = ce.coin_environment(pheads)

#%% Repetition and trials

Epsilon = np.arange(.01, .11, .01)
trials = 1000
repetition = 100
mean_every_trial = np.empty(len(Epsilon))
stdev_every_trial = np.empty(len(Epsilon))

for a in range (len(Epsilon)):
    total_every_trial = np.zeros(repetition)
    
    for l in range (repetition):
        Sum = np.zeros(len(pheads))
        Times = np.zeros(len(pheads))
        
        for i in range (1, len(pheads) + 1):
            if (coin.flip(i) == "heads"):
                Sum[i-1] += 1
            Times[i-1] += 1
    
        successRate = Sum/Times

        for y in range (trials - len(pheads)):
            number = np.random.rand()
            if (number <= Epsilon[a]):
                randomCoin = np.random.choice(len(pheads) + 1)
                if (coin.flip(randomCoin) == "heads"):
                    Sum[randomCoin-1] += 1
            
                Times[randomCoin-1] += 1
        
            else: 
                
                highest = np.random.choice(np.where(successRate == np.max(successRate)) [0]) 
                if (coin.flip(highest + 1) == "heads"):
                    Sum[highest] += 1
            
                Times[highest] += 1
        
            successRate = Sum/Times
            
        total_every_trial[l] = np.sum(Sum)
        
    mean_every_trial[a] = np.mean(total_every_trial)
    stdev_every_trial[a] = np.std(total_every_trial)
    
print ("Total Number of heads" + str(Sum))

Index = np.argmax(mean_every_trial)
right_epsilon = Epsilon[Index]
mean_right_epsilon = mean_every_trial[Index]
stdev_right_epsilon = stdev_every_trial[Index]

#%% saving data pheads
io.savemat("Epsilon" + str(pheads) + "_" + str(repetition) + "_" + str(trials) + "Data.mat", {"right_epsilon": right_epsilon, 
                               "mean_right_epsilon": mean_right_epsilon,
                               "stdev_right_epsilon": stdev_right_epsilon})

#%% Make a plot 
plt.figure()

plt.errorbar(Epsilon, mean_every_trial, yerr = stdev_every_trial,
             fmt='-o', ecolor='orangered', capsize=2)

plt.xlabel('Epsilon')
plt.ylabel('Total Heads')
plt.title('Epsilon Results: Mean +/- Standard Deviation')
plt.grid(True)

#for loop 3
#flip each coin one time
#Calculate success rate of each coin
#Find highest successs rate
#for loop 97
#Based on probabilty either random or choice
#Output best coin with highest success rate, and total number of heads

