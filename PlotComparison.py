# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:51:14 2020

@author: student-minecraft
"""
import matplotlib.pyplot as plt
import scipy.io as io
import numpy as np

pheads = np.array([0.52,0.5,0.55,0.47])
repetition = 500
trials = 1000

explore_exploit = io.loadmat("ExploreExploit" + str(pheads) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")
epsilon = io.loadmat("Epsilon" + str(pheads) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")
epsilonGreedy=io.loadmat("EpsilonGreedy" + str(pheads) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")

mean = np.array([explore_exploit["mean_right_explore"][0][0], epsilon["mean_right_epsilon"][0][0], 
                 epsilonGreedy["mean_right_epsilon"][0][0]])
stdev = np.array([explore_exploit["stdev_right_explore"][0][0], epsilon["stdev_right_epsilon"][0][0],
                 epsilonGreedy["stdev_right_epsilon"][0][0]])

xvalues = np.arange(len(mean))

plt.figure()

plt.errorbar(xvalues, mean, 
             yerr = stdev,
             fmt='-o', ecolor='orangered', capsize=2)

plt.xlabel('Method')
plt.ylabel('Total Heads')
plt.title('Comparing')
plt.xticks(xvalues, ["Explore Exploit", "Epsilon Greedy", "Epsilon Decay"])