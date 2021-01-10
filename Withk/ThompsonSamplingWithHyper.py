# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:05:29 2020

@author: Alyssa
"""
import CoinEnvironmentWithK as cek
import numpy as np
import scipy.io as io
from scipy.stats import norm, beta

k = 20
c = 0.1
ProbBestCoin = 0.5
hyper = np.array([0.5, 0.52, 0.55, 0.58, 0.6, 0.62, 0.65, 0.68, 0.7])

coin = cek.coin_environment_k(k, c, ProbBestCoin)

repetition = 100 #make smaller
trials = 20000 #make bigger 

regret_every_trial = []
mean_every_trial = np.empty(len(hyper))
stdev_every_trial = np.empty(len(hyper))

def sample (s, ttf, h):
    a = 1
    b = 1
    samples = np.zeros(k)
    for c in range (k):
        samples[c] = np.random.beta(a + h * s[c], b + h * (ttf[c] - s[c])) 
        
    highest = np.random.choice(np.where(samples == np.max(samples)) [0])
    return highest

for h in range (len(hyper)):

    arr = np.zeros((trials, repetition))
    regret_arr = np.ones((trials, repetition))/2
    total_every_trial = np.empty(repetition)

    for l in range (repetition):

        Sum = np.zeros(k)
        total_trials_finished = np.zeros(k)
    
        for y in range (trials):
        
            highest = sample(Sum, total_trials_finished, h)
            if (coin.flip(highest) == "heads"):
                Sum[highest] += 1
                arr[y][l] = 1

            total_trials_finished[highest] +=1
        
        total_every_trial[l] = np.sum(Sum)
    

    regret_every_trial.append(np.cumsum((regret_arr - arr), axis = 0))
    mean_every_trial[h] = np.mean(total_every_trial)
    stdev_every_trial[h] = np.std(total_every_trial)
    
Index = np.argmax(mean_every_trial)
right_hyperparameter = hyper[Index]
#%%

io.savemat("ThompsonSamplingWithHyper" + str(k) + "_" + str(repetition) + "_" + str(trials) + 
           "_" + str(right_hyperparameter) + "Data.mat", 
           { "right_hyperparameter": right_hyperparameter,
            "regret": regret_every_trial[Index],
            "mean": mean_every_trial[Index], 
            "stdev": stdev_every_trial[Index]})

#%%

TSH = io.loadmat("ThompsonSamplingWithHyper" + str(k) + "_" + str(repetition) + "_" + str(trials) + 
           "_" + str(right_hyperparameter) + "Data.mat")

print(TSH["right_hyperparameter"])
    