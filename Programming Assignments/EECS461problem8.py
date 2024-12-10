"""
Dylan Davis
3047302
461 ID:54
10 October 2023
HomeWork 7 Problem 8
"""

import random
import math

# set variable values
lamba = 1.0
mu = 3.0
sig = 1.0
delta = 0.01

# The number of samples
n = 100000

# lists to store counts
expCount = [0] * 501  # i = 0 to 500
gCount = [0] * 601  # i = 0 to 600

# Random sample
expSample = [random.expovariate(lamba) for i in range(n)]
gSample = [random.normalvariate(mu, sig) for i in range(n)]

# Count Occurances
for i in range(501):
    lower_bound = i * delta
    upper_bound = (i + 1) * delta
    expCount[i] = sum(1 for i in expSample if lower_bound <= i < upper_bound)

for i in range(601):
    lower_bound = i * delta
    upper_bound = (i + 1) * delta
    gCount[i] = sum(1 for i in gSample if lower_bound <= i < upper_bound)
# calculations
left_exp = [count / n for count in expCount]
right_exp = [lamba * math.exp(-lamba * i * delta) * delta for i in range(501)]

# calculates left/right side of equation for gaussian distribution
left_g = [count / n for count in gCount]
right_g = [(1 / (sig * math.sqrt(2 * math.pi))) * \
                math.exp(-0.5 * ((mu - i * delta) / sig) ** 2) * delta for i in range(601)]

# given values
values = [0, 100, 200, 300, 400, 500]

print("=====Exponential Distribution=====")
for i in values:
    print ("i = " + str(i) + ": \n" +" Left side = " + str(left_exp[i]) + ", Right side = " + str(right_exp[i]))

print("\n=====Gaussian Distribution=====")
for i in values:
    print ("i = " + str(i) + ": \n" +" Left side = " + str(left_g[i]) + ", Right side = " + str(right_g[i]))


