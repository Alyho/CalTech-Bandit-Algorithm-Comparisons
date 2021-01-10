# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:40:42 2020

@author: student-minecraft
"""

import numpy as np

class coin_environment_k:

    def __init__(self, k, c, ProbBestCoin):
        self.prob_heads = np.zeros(k)
        self.prob_heads[0] = ProbBestCoin
        for i in range (k-1):
           self.prob_heads[i+1] = ProbBestCoin - c 
        
    def flip(self, coin_number):
        random_number = np.random.choice([0,1], p=[1-self.prob_heads[coin_number-1], self.prob_heads[coin_number-1]])
        
        if random_number == 1:
            return "heads"
        else:
            return "tails"
    
#coin = coin_environment_k()

