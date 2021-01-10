# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:19:59 2020

@author: student-minecraft
"""
import matplotlib.pyplot as plt
import scipy.io as io
import numpy as np

k = 20
repetition = 100
trials = 20000

exploreExploit = io.loadmat("Explore_exploit_results.mat")
epsilon = io.loadmat("Epsilon_greedy_results.mat")
epsilonDecay=io.loadmat("Epsilon_decay_results.mat")
upperBound = io.loadmat("kUpperBound" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")

meanEE = exploreExploit[""]

xvalues = np.arange(len(mean))

plt.figure()

plt.errorbar(xvalues, mean, 
             yerr = stdev,
             fmt='-o', ecolor='orangered', capsize=2)

plt.xlabel('Method')
plt.ylabel('Total Heads')
plt.title('Comparing')
plt.xticks(xvalues, ["Explore Exploit", "Epsilon Greedy", "Epsilon Decay", "UpperBound"])