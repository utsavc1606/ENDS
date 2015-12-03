'''
Created on Dec 3, 2015

@author: utsavchatterjee

This program counts the number of tweets posted by each user. 
'''
import collections

# Common directory where all files are located; storing into variable for convenience
filesDirectory = "/Users/utsavchatterjee/Documents/Python Projects/ENDS Tweet Analysis/ENDS/Data/"

# storing the necessary files into variables and opening them for read/write operations
cleanDataFile = open(filesDirectory+"spamFreeData.txt", "r")
outputFile = open(filesDirectory+"userFrequency.txt", "w")


# defining the level thresholds for tweets by users
highFrequencyLimit = 50
medFrequencyLimit = 25
lowFrequencyLimit = 10

# Defining counters
highCounter = 0
medCounter = 0
lowCounter = 0

# loading all users into a list
userList = []
for users in cleanDataFile:
    userList.append(users.split("-->")[0])
    
# Counting frequency per tweet in the entire data set. Only high frequency tweets (>3 frequency) have been filtered out.  
counter = collections.Counter(userList)

outputFile.write("---------------HIGH FREQUENCY USERS----------------- \n")
for items in counter.iteritems():
    if items[1] > highFrequencyLimit:
        outputFile.write(items[0].strip("\n")+"|"+str(items[1])+"\n")
        highCounter += 1
        
outputFile.write("---------------MEDIUM FREQUENCY USERS----------------- \n")        
for items in counter.iteritems():
    if items[1] >medFrequencyLimit:
        outputFile.write(items[0].strip("\n")+"|"+str(items[1])+"\n")
        medCounter += 1
    
outputFile.write("---------------LOW FREQUENCY USERS----------------- \n")        
for items in counter.iteritems():
    if items[1] <lowFrequencyLimit:
        outputFile.write(items[0].strip("\n")+"|"+str(items[1])+"\n")
        lowCounter += 1
        
outputFile.write( " \n High Frequency Users: " + str(highCounter) +"\n")
outputFile.write( "Medium Frequency Users: " + str(medCounter)+"\n")
outputFile.write( "Low Frequency Users: " + str(lowCounter)    +"\n")    
            

