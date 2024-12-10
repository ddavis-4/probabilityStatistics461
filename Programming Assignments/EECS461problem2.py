#completed in python
'''
Dylan Davis 
3047302
EECS 461
11/21/2023
problem 2 from homework 13 
'''
# imports 
import numpy as np
import matplotlib.pyplot as plt

rand_num = np.random.rand(10000) 
# creates a variable, that generates an array of 10,000 random numbers sampling uniform(0,1) 

transformed_rand_num = -2 * np.log(1 - rand_num) 
# converts the randomly generated numbers into expeonetial distribution and sets the mean to 2, 


bin_size = 0.1 # sets the size of each bin to .1
edges = np.arange(0, 10.1, bin_size) # generates values from 0 to 10, and increments by the size of the bins this creates edges for the bins in histogram
hValues, _ = np.histogram(transformed_rand_num, bins = edges, density = True) #histogram is created for the now transformed samples of random numbers 

theoreticProb = np.exp(-edges[:-1] / 2) - np.exp(-(edges[:-1] + bin_size) / 2) 
# This Calculates the theoretical probabilities for the exponential distribution

# ----------plotting ----------
fig, axs = plt.subplots(1, 2, figsize=(12, 5)) 
# This creates figure & pair of subplots using the matplotlib import, 
# and it allows for the two histograms to be presented at the same time side by side.

# generated value ---------- plots
axs[0].bar(edges[:-1], hValues, width = bin_size, align = 'edge') # this will plot a bar chart using the edges as its x-values while the histogram values are used for the y values.
#labels for graph 
axs[0].set_xlabel('Value Bins')  
axs[0].set_ylabel('Probability') 
axs[0].set_title('Histogram of Transformed Exponential Samples')  
axs[0].grid(True) # enable grib for graph 

# Theoretic -------------- plots 
axs[1].bar(edges[:-1], theoreticProb, width = bin_size, align = 'edge') # this line plots bar chart using edges as x-values like before, and the y values are the theoratic probs.
#labels for axis and graph
axs[1].set_xlabel('Value Bins')  
axs[1].set_ylabel('Probability')  
axs[1].set_title('Theoretical Probability of Exponential Samples when (mean = 2)')  
axs[1].grid(True) # same as before 

plt.tight_layout() # adjust layout 
plt.show() # show the plots 
