"""
Dylan Davis | 3047302
9/19/2023
EECS 461: Probability and Statistics
Assignment 4 Problem 1
"""

import random

# define variables
# the probability of a 0 being received as a 1
errorProb0_1 = 0.03
# the probability of a 1 being received as a 0
errorProb1_0 = 0.01
# number of packets
packets = 250
# number of bits per package
packetBits = 150
# start with 0 packets correctly decoded
correctPackets = 0


# function to decode packets, or to simulate decoding them.
def decode_packet():
    error = 0  # error starts at 0 because no packets have been decoded incorrectly

    for i in range(packetBits):  # for i in the 150 bits per package
        bit_t = random.choice([0, 1])  # the transmitted bit is == to a random choice between 0 and 1

        bit_r = bit_t  # the bit transmitted is == to the bit received use random to help simulate when error occurs
        if bit_t == 0:
            if random.random() < errorProb0_1:
                bit_r = 1
        else:
            if random.random() < errorProb1_0:
                bit_r = 0
        if bit_r != bit_t:
            error += 1
    if error <= 5:  # as long as the error is less than or equal to 5 the packet is decoded
        return True
    return False


# for loop that for every packet that comes in if it is decoded then 1 is added to the packets decoded correctly
for i in range(packets):
    if decode_packet():
        correctPackets += 1

# calculate the probabilities
RF_correctPackets = correctPackets / packets
theoProb = 1 - ((1 - errorProb0_1) ** packetBits)

print('Number of correctly decoded packets:', correctPackets)
print('The relative frequency of correctly decoded packets:', RF_correctPackets)
print('The theoretical probability of a packet being correctly decoded:', theoProb)

