# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:58:56 2019

@author: student-minecraft
"""
import numpy as np
import Coin_Environment as ce
import time

t1 = time.time()

coin = ce.coin_environment()

array = np.zeros(3)

for i in range(1, 4):
    
    for n in range (200):
        
        if (coin.flip(i) == "heads"):
            array[i-1] += 1
     
    #print ("Coin" + str(i) + " = " + str(total_current) + " heads")   

total_number_of_heads = np.sum(array)
best_coin = np.argmax(array) + 1

for y in range (400): 
    
    if(coin.flip(best_coin) == "heads"):
        total_number_of_heads += 1
     
print ("Total number" +  " = " + str(total_number_of_heads) + " heads")   

t2 = time.time()

print (t2 - t1)
    
    
    
    
    