# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:58:56 2019

@author: student-minecraft
"""

import Coin_Environment as ce
import time

t1 = time.time()

coin = ce.coin_environment()

total_updated = 0
best_coin = 0
total_number_of_heads = 0

for i in range(1, 4):
    
    total_current = 0
    
    for n in range (200):
        
        if (coin.flip(i) == "heads"):
            total_current += 1
            total_number_of_heads += 1
     
    #print ("Coin" + str(i) + " = " + str(total_current) + " heads")   
    
    if (total_current > total_updated):
         total_updated = total_current
         best_coin = i
         
for y in range (400): 
    coin.flip(best_coin)
    
    if(coin.flip(i) == "heads"):
            total_number_of_heads += 1
     
print ("Total number" +  " = " + str(total_number_of_heads) + " heads")   

t2 = time.time()

print (t2 - t1)
    
    
    
    
    