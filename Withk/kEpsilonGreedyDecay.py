# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:08:35 2020

@author: student-minecraft
"""

import CoinEnvironmentWithK as cek
import numpy as np
import scipy.io as io

k = 20
c = 0.1
ProbBestCoin = 0.5

coin = cek.coin_environment_k(k,c,ProbBestCoin)

hyperparameter = np.array([200, 500, 800])
trials = 20000
repetition = 100
regret = []
mean_every_trial = np.empty(len(hyperparameter))
stdev_every_trial = np.empty(len(hyperparameter))
Epsilon = 1

for a in range (len(hyperparameter)):
    total_every_trial = np.zeros(repetition)
    regret_arr = np.ones((trials, repetition))/2
    arr = np.zeros((trials, repetition))
    
    for l in range (repetition):
        Sum = np.zeros(k)
        Times = np.zeros(k)
        
        for i in range (1, k + 1):
            if (coin.flip(i) == "heads"):
                Sum[i-1] += 1
                arr[i-1][l] = 1
            Times[i-1] += 1
    
        successRate = Sum/Times

        for y in range (trials - k):
            number = np.random.rand()
            if (number <= Epsilon):
                randomCoin = np.random.choice(k + 1)
                if (coin.flip(randomCoin) == "heads"):
                    Sum[randomCoin-1] += 1
                    arr[y-1][l] = 1
            
                Times[randomCoin-1] += 1
        
            else: 
                
                highest = np.random.choice(np.where(successRate == np.max(successRate)) [0]) 
                if (coin.flip(highest + 1) == "heads"):
                    Sum[highest] += 1
                    arr[y-1][l] = 1
            
                Times[highest] += 1
        
            successRate = Sum/Times
            Epsilon = hyperparameter[a]/ (hyperparameter[a] + np.sum(Times))
            
        total_every_trial[l] = np.sum(Sum)
        
    mean_every_trial[a] = np.mean(total_every_trial)
    stdev_every_trial[a] = np.std(total_every_trial)
    regret.append(np.cumsum((regret_arr - arr), axis = 0))
    
print ("Total Number of heads" + str(Sum))

Index = np.argmax(mean_every_trial)
right_hyperparameter = hyperparameter[Index]
mean_right_epsilon = mean_every_trial[Index]
stdev_right_epsilon = stdev_every_trial[Index]
    
#%% saving data cek

io.savemat("kEpsilonGreedy" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat", 
           {"right_hyperparameter": right_hyperparameter, 
                               "mean_right_epsilon": mean_right_epsilon,
                               "stdev_right_epsilon": stdev_right_epsilon,
                               "regret": regret[Index]})