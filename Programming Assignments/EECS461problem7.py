"""
Dylan Davis
Tue Sep 5
Explanation:
this program will generate 1,500 scores from 51 to 100, where each score is
equally likely and independent of the others. Also, the program will calculate the percentage of A scores among
the 1,500 scores generated, and have the program print the first 30 scores generated.
"""
import random # allows us to use random 


scores = [] # list of all the possible scores (1,500)
alist = [] #list of all the a scores. Both are empty. 

CountTo30 = 1 # a varaiable that will help us return the first 30 values  

while len(scores) < 1500: #a loop that will run as long as the length of the list scores is less than 1,500
    score = random.randint(51,100) # this line generates the scores, so any random integer between 51 and 100 is a possiblitiy
    scores.append(score) # adds to the list scores the values generated (score)
    if score >= 90: # if the value of the score generated in greater than 90 (an A) it is added to the a list
        alist.append(score) # scores 90 or above added to the 'a list' 
    if CountTo30 < 31: 3 #as long as the count is less than 31 then the score is printed and 1 is added to 'CountTo30'
        print(score)
        CountTo30 = CountTo30 + 1

probofgettinganA = (11/50)*100 #this is the calculated probablity of getting an A
probofA = (len(alist)/len(scores)) * 100 #this will give us the actual probablity of getting an a each list generated

print( 'The calculated probablilty of getting an A: ' + str(probofgettinganA)) #this prints the probablities of getting an A that are calculated above.
print( "The precentage of A's out of the generated: " + str(probofA) + '%')


        
