# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:40:36 2019

@author: student-minecraft
"""


import numpy as np

class coin_environment:

    def __init__(self, probability = []):
       self.prob_heads = probability
        
    def flip(self, coin_number):
        random_number = np.random.choice([0,1], p=[1-self.prob_heads[coin_number-1], self.prob_heads[coin_number-1]])
        
        if random_number == 1:
            return "heads"
        else:
            return "tails"
    
coin = coin_environment()

#print ("Coin 1 = " + coin.flip(1))
#print ("Coin 2 = " + coin.flip(2))
#print ("Coin 3 = " + coin.flip(3))        
    