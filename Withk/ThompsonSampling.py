# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:22:22 2020

@author: Alyssa
"""
import CoinEnvironmentWithK as cek
import numpy as np
import scipy.io as io
from scipy.stats import norm, beta

k = 20
c = 0.1
ProbBestCoin = 0.5

coin = cek.coin_environment_k(k, c, ProbBestCoin)

repetition = 100 #make smaller
trials = 20000 #make bigger 
    
arr = np.zeros((trials, repetition))
regret_arr = np.ones((trials, repetition))/2
total_every_trial = np.empty(repetition)

def sample (s, ttf):
    a = 1
    b = 1
    samples = np.zeros(k)
    for c in range (k):
        samples[c] = np.random.beta(a + s[c], b + (ttf[c] - s[c])) 
        
    highest = np.random.choice(np.where(samples == np.max(samples)) [0])
    return highest

for l in range (repetition):

    Sum = np.zeros(k)
    total_trials_finished = np.zeros(k)
    
    for y in range (trials):
        
        highest = sample(Sum, total_trials_finished)
        if (coin.flip(highest) == "heads"):
            Sum[highest] += 1
            arr[y][l] = 1

        total_trials_finished[highest] +=1
        
    total_every_trial[l] = np.sum(Sum)
    

regret = np.cumsum((regret_arr - arr), axis = 0)
mean = np.mean(total_every_trial)
stdev = np.std(total_every_trial)

#%%

io.savemat("ThompsonSampling" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat", 
           { "total_every_trial": total_every_trial, "regret": regret,
            "mean": mean, 
            "stdev": stdev})



    