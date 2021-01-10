# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:37:42 2020

@author: student-minecraft
"""

import CoinEnvironmentWithK as cek
import numpy as np
import scipy.io as io


k = 20
c = 0.1
ProbBestCoin = 0.5
a = [0.243, 0.242, 0.241, 0.24, 0.239, 0.238]

coin = cek.coin_environment_k(k, c, ProbBestCoin)

repetition = 100 #make smaller
trials = 20000 #make bigger 
big_array = []
regret = []
mean_every_trial = np.empty(len(a))
stdev_every_trial = np.empty(len(a))

def explore (action):
    if (Times_picked_action[action] != 0):
        explore_sum = ((2 * np.log(total_trials_finished)) / Times_picked_action[action]) ** 0.5
    else: 
        explore_sum = 0
        
    return explore_sum
    
for b in range (len(a)):

    arr = np.zeros((trials, repetition))
    regret_arr = np.ones((trials, repetition))/2
    total_every_trial = np.empty(repetition)

    for l in range (repetition):
        Sum = np.zeros(k)
        total_trials_finished = 0
        Times_picked_action = np.zeros(k)
        Explore_sum = np.zeros(k)
    
        for i in range (1, k+1):
            if (coin.flip(i) == "heads"):
                Sum[i-1] += 1
                arr[i-1][l] = 1
                
            Times_picked_action[i-1] += 1
            total_trials_finished +=1
            
            for j in range (k):
                Explore_sum[j] = explore(j)
            
        successRate = Sum / Times_picked_action
    
        UpperBound= successRate + Explore_sum * a[b]  
    
        for y in range (k, trials + 1):
        
            selectedAction = np.argmax(UpperBound)
            if (coin.flip(selectedAction + 1) == "heads"):
                Sum[selectedAction] += 1
                arr[y-1][l] = 1
        
            Times_picked_action[selectedAction] += 1
            total_trials_finished +=1
        
            for c in range (k):
                Explore_sum[c] = explore(c)
            
            successRate = Sum / Times_picked_action
    
            UpperBound= successRate + Explore_sum * a[b]
    
        total_every_trial[l] = np.sum(Sum)
    
    big_array.append(arr)
    regret.append(np.cumsum((regret_arr - arr), axis = 0))
    mean_every_trial[b] = np.mean(total_every_trial)
    stdev_every_trial[b] = np.std(total_every_trial)
    
best_hyper = np.argmax(mean_every_trial)
print(a[best_hyper])
print(big_array[best_hyper])
print(regret[best_hyper])
io.savemat("kUpperBound" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat", 
           { "big_array_ucb": big_array[best_hyper], "regret": regret[best_hyper],
            "best hyper": a[best_hyper], "mean_every_trial": mean_every_trial, 
            "stdev_every_trial": stdev_every_trial})



    