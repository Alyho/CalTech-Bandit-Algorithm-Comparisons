# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:58:18 2020

@author: student-minecraft
"""

import numpy as np
import Coin_Environment as ce
#Epsilon greedy
#has to find success rate
#array of just sum and number of times

#for loop generates random number
#find mean of all the random numbers without storing them all
#every loop store sum and times

Sum = np.zeros(3)
Times = np.zeros(3)

coin = ce.coin_environment()

Epsilon = .05
Trials = 100

for i in range (1,4):
    if (coin.flip(i) == "heads"):
        Sum[i-1] += 1
    Times[i-1] += 1
    
successRate = Sum/Times

for y in range (Trials - 3):
    number = np.random.rand()
    if (number <= Epsilon):
        randomCoin = np.random.choice([1,2,3])
        if (coin.flip(randomCoin) == "heads"):
            Sum[randomCoin-1] += 1
            
        Times[randomCoin-1] += 1
        
    else: 
        
        highest = np.random.choice(np.where(successRate == np.max(successRate)) [0]) 
        if (coin.flip(highest + 1) == "heads"):
            Sum[highest] += 1
            
        Times[highest] += 1
        
    successRate = Sum/Times
    
#print ("Best coin with highest success rate" + np.where(successRate == np.max(successRate)) [0])
print ("Total Number of heads" + str(Sum))

#for loop 3
#flip each coin one time
#Calculate success rate of each coin
#Find highest successs rate
#for loop 97
#Based on probabilty either random or choice
#Output best coin with highest success rate, and total number of heads

