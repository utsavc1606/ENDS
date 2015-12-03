'''
Created on Dec 2, 2015

@author: utsavchatterjee

This piece of code removes all retweeted (RT) tags from tweets so that only user id and main 
tweet text is left with for further analysis.

'''
inputFile = open("/Users/utsavchatterjee/Documents/Python Projects/ENDS Tweet Analysis/ENDS/testdata.txt", "r")
outputFile = open("/Users/utsavchatterjee/Documents/Python Projects/ENDS Tweet Analysis/ENDS/retweets.txt", "w")

rtMarker = "RT @"
for line in inputFile:
    tweetText = line.split("-->")[1]
    username = line.split("-->")[0]
    if rtMarker in tweetText:
        try:
            outputFile.write(username+" --> " + tweetText.split(":",1)[1])
        except:
            outputFile.write("error encountered here")
            pass
    else:
        outputFile.write(username+" --> " + tweetText)
        
inputFile.close()
outputFile.close()

