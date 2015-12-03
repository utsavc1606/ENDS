'''
Created on Dec 3, 2015

@author: utsavchatterjee

This program reads from the list of unwanted tweets, then reads the entire data file (tweets collected) and filters out clean non-spam tweets 
into a new text file.
'''
# Common directory where all files are located; storing into variable for convenience
filesDirectory = "/Users/utsavchatterjee/Documents/Python Projects/ENDS Tweet Analysis/ENDS/Data/"

#other variables
spamCount = 0
cleanCount = 0

# storing the necessary files into variables and opening them for read/write operations
unwantedFile = open(filesDirectory+"unwantedTweets.txt", "r")
dataFile = open(filesDirectory+"Step2Op4Staging.txt", "r")
outputFile1 = open(filesDirectory+"spamFreeData.txt", "w")

# Create a list for storing unwanted tweets
spamList = []

# Load all unwanted tweets into a list
for tweets in unwantedFile:
    spamList.append(tweets)
    
# Read the data file line by line and if a line does not exist in the list, print it out to a new file as a god tweet
for lines in dataFile:
    if lines.split("-->")[1].lstrip() in spamList:
        print lines + "spam"
        spamCount +=1
    else:
        outputFile1.write(lines)
        cleanCount +=1
        
print "Spam tweets filtered: "+ str(spamCount)
print "Clean tweets filtered: "+ str(cleanCount)        
