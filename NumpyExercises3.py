# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:56:57 2020

@author: student-minecraft
"""

import numpy as np 

array = np.arange(6)
print(len(array))

#3 - Using only one function call, generate 4 random numbers uniformly-distributed between 9 and 15
array = 6 * np.random.rand(4) + 9 
print(array)

#4 Using only one function call, generate 3 random numbers uniformly-distributed between -5 and 4 
array = 9 * np.random.rand(3) + -5
print(array)

#5 Determining how many times a flipped unfair coin lands on heads.

def flip(trials): 
    unfair = 0.3 
    array = np.empty(trials)

    for y in range (trials): 
        flip = np.random.rand()
    
        if flip > unfair : 
            array[y] = 0
        else:
            array[y] = 1
    
    tails = np.where(array == 0)[0]
    print(tails)    
    
    heads = np.where(array == 1)[0]
    print(heads)
    return len(heads)

print(flip(100))

#6 Generate 100 numbers between 0 and 100. How many of them are above 70? How many of them are below 70?
array = 100 * np.random.rand(100)
print(array)

below = np.where(array < 70)[0]
print(len(below))
print(100 - len(below))

#7 Return to coin example from 3. Find the fraction of the flips that land on heads. 

NumberTrials = np.array([10, 50, 100, 500, 1000, 10000, 100000])
fraction = np.zeros(len(NumberTrials))

for n in range (len(NumberTrials)):
    NumberHeads = flip(NumberTrials[n])
    fraction[n] = NumberHeads / NumberTrials[n]
 
print(fraction)
