'''
Created on Dec 3, 2015

@author: utsavchatterjee

This program filters takes the output from Step 2 as input (AllTweetsNoRtTag.txt) and creates two output files unwantedTweets.txt and 
unwantedTweetsWithFrequency.txt. The first output file is simply a list of all suspected spam tweets as per our filter and 
the second output file contains the tweet frequency of each spam tweet from the whole data set. 
'''
import collections

# Common directory where all files are located; storing into variable for convenience
filesDirectory = "/Users/utsavchatterjee/Documents/Python Projects/ENDS Tweet Analysis/ENDS/Data/"

# storing the necessary files into variables and opening them for read/write operations 
inputFile = open(filesDirectory+"Step2Op4Staging.txt", "r")
outputFile1 = open(filesDirectory+"unwantedTweets.txt", "w")
outputFile2 = open(filesDirectory+"unwantedTweetsWithFrequency.txt", "w")

# Create list in which to load all tweets text only (no user id). This is because the purpose is simply to filter out spam tweets
tweetList = []
for line in inputFile:
    tweetText = line.split("-->")[1]
    tweetList.append(tweetText)

# Counting frequency per tweet in the entire data set. Only high frequency tweets (>3 frequency) have been filtered out.  
counter = collections.Counter(tweetList)
for items in counter.iteritems():
    if items[1] > 3:
        outputFile1.write(items[0].lstrip())
        concatString = (items[0].strip("\n")+"|"+str(items[1])+"\n")
        outputFile2.write(concatString.lstrip())

# Closing files
inputFile.close()
outputFile1.close()
outputFile2.close()

