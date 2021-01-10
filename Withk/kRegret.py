# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:46:32 2020

@author: student-minecraft
"""

import matplotlib.pyplot as plt
import scipy.io as io
import numpy as np
#%%
k = 20
repetition = 100
trials = 20000
right_hyperparameter = 0.58

regret_arr = np.ones((trials, repetition))/2

thompsonSampling = io.loadmat("ThompsonSampling" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")
regretTS = thompsonSampling["regret"]

thompsonSamplingHyper = io.loadmat("ThompsonSamplingWithHyper" + str(k) + "_" + str(repetition) + "_" + str(trials) + "_" + str(right_hyperparameter) + "Data.mat")
regretTSH = thompsonSamplingHyper["regret"]

upperBound = io.loadmat("kUpperBound" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")
regretUCB = upperBound["regret"]

EpsilonGreedyDecay = io.loadmat("kEpsilonGreedy" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")
regretEGD = EpsilonGreedyDecay["regret"]

EpsilonGreedyRep = io.loadmat("kEpsilon" + str(k) + "_" + str(repetition) + "_" + str(trials) + "Data.mat")
regretEGR = EpsilonGreedyRep["regret"]

ExploreExploit = io.loadmat("Explore_exploit_results.mat")
bigarray = ExploreExploit["flip_outcomes"]
regretEE = np.cumsum((regret_arr - bigarray), axis = 0)

meanUCB = np.empty(trials)
stdevUCB = np.empty(trials)
meanEGD = np.empty(trials)
stdevEGD = np.empty(trials)
meanEGR = np.empty(trials)
stdevEGR = np.empty(trials)
meanTS= np.empty(trials)
stdevTS = np.empty(trials)
meanTSH= np.empty(trials)
stdevTSH = np.empty(trials)
meanEE= np.empty(trials)
stdevEE = np.empty(trials)

for g in range (trials):
    meanUCB[g] = np.mean(regretUCB[g])
    stdevUCB[g] = np.std(regretUCB[g])
    meanEGD[g] = np.mean(regretEGD[g])
    stdevEGD[g] = np.std(regretEGD[g])
    meanEGR[g] = np.mean(regretEGR[g])
    stdevEGR[g] = np.std(regretEGR[g])
    meanTS[g] = np.mean(regretTS[g])
    stdevTS[g] = np.std(regretTS[g])
    meanTSH[g] = np.mean(regretTSH[g])
    stdevTSH[g] = np.std(regretTSH[g])
    meanEE[g] = np.mean(regretEE[g])
    stdevEE[g] = np.std(regretEE[g])

plt.figure()

plt.plot(np.arange(1, trials + 1), meanEGD, color = 'green')
plt.fill_between(np.arange(1, trials + 1), meanEGD -   
	stdevEGD, meanEGD + stdevEGD, alpha = 0.1, color = 'green')

plt.plot(np.arange(1, trials + 1), meanEGR, color = 'orange')
plt.fill_between(np.arange(1, trials + 1), meanEGR -   
	stdevEGR, meanEGR + stdevEGR, alpha = 0.1, color = 'orange')

plt.plot(np.arange(1, trials + 1), meanTS, color = 'red')
plt.fill_between(np.arange(1, trials + 1), meanTS -   
	stdevTS, meanTS + stdevTS, alpha = 0.1, color = 'red')

plt.plot(np.arange(1, trials + 1), meanTSH, color = 'black')
plt.fill_between(np.arange(1, trials + 1), meanTSH -   
	stdevTSH, meanTSH + stdevTSH, alpha = 0.1, color = 'black')

plt.plot(np.arange(1, trials + 1), meanUCB, color = 'blue')
plt.fill_between(np.arange(1, trials + 1), meanUCB -   
	stdevUCB, meanUCB + stdevUCB, alpha = 0.1, color = 'blue')

plt.plot(np.arange(1, trials + 1), meanEE, color = 'purple')
plt.fill_between(np.arange(1, trials + 1), meanEE -   
	stdevEE, meanEE + stdevEE, alpha = 0.1, color = 'purple')

plt.legend(["Epsilon Greedy Decay", "Epsilon Greedy Repetition", "Thompson Sampling", 
            "Thompson Sampling W/HP",
            "Upper Confidence Bound", 
            "Explore Exploit"], loc="upper left")

plt.xlabel('Trials')
plt.ylabel('Total Heads')
plt.title('Comparing Regret')


#%%
num_errorbars = 15     # Number of error bars to draw on the plot.

# Determine x-locations at which to draw the error bars. This is done by picking
# num_errorbars equally-spaced points in x. So that the error bars are not 
# drawn right at the edges of the plot, we can add 2 to the number of error 
# bars, and then chop off the 1st and last locations (via "[1: -1]"). The chopped-
# off locations are all the way at the left and right of the plot.
errorbar_x = np.linspace(1, trials, num_errorbars + 2)[1: -1]
errorbar_x = np.round(errorbar_x).astype(int)   # Round to nearest integer

plt.figure()

plt.plot(np.arange(1, trials + 1), meanEGD, color = 'green')
plt.errorbar(errorbar_x, meanEGD[errorbar_x], yerr = stdevEGD[errorbar_x], 
             fmt='o', color = 'green', ecolor='green', capsize=5,
             linewidth = 2, capthick = 2)

plt.plot(np.arange(1, trials + 1), meanEGR, color = 'orange')
plt.errorbar(errorbar_x, meanEGR[errorbar_x], yerr = stdevEGR[errorbar_x], 
             fmt='o', color = 'orange', ecolor='orange', capsize=5,
             linewidth = 2, capthick = 2)

plt.plot(np.arange(1, trials + 1), meanEE, color = 'purple')
plt.errorbar(errorbar_x, meanEE[errorbar_x], yerr = stdevEE[errorbar_x], 
             fmt='o', color = 'purple', ecolor='purple', capsize=5,
             linewidth = 2, capthick = 2)

plt.legend(["Epsilon Greedy Decay", "Epsilon Greedy Repetition", "Explore Exploit"], loc="upper left")
plt.xlabel('Trials')
plt.ylabel('Total Heads')
plt.title('Comparing Regret')

plt.figure()
plt.plot(np.arange(1, trials + 1), meanTS, color = 'red')
plt.errorbar(errorbar_x, meanTS[errorbar_x], yerr = stdevTS[errorbar_x], 
             fmt='o', color = 'red', ecolor='red', capsize=5,
             linewidth = 2, capthick = 2)

plt.plot(np.arange(1, trials + 1), meanTSH, color = 'black')
plt.errorbar(errorbar_x, meanTSH[errorbar_x], yerr = stdevTSH[errorbar_x], 
             fmt='o', color = 'black', ecolor='black', capsize=5,
             linewidth = 2, capthick = 2)

plt.plot(np.arange(1, trials + 1), meanUCB, color = 'blue')
plt.errorbar(errorbar_x, meanUCB[errorbar_x], yerr = stdevUCB[errorbar_x], 
             fmt='o', color = 'blue', ecolor='blue', capsize=5,
             linewidth = 2, capthick = 2)
plt.legend(["Thompson Sampling", "Thompson Sampling w/H", "Upper Confidence Bound"], loc="upper left")

plt.xlabel('Trials')
plt.ylabel('Total Heads')
plt.title('Comparing Regret')
