'''
Created on Dec 12, 2015

@author: utsavchatterjee
'''
import re
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()


dataPath = "/Users/utsavchatterjee/Documents/Python Projects/ENDS Tweet Analysis/ENDS/Data/"
inputFileName = "spamFreeData.txt"
outputFileName = "tweetsWithSentiment.txt"
progressCounter = 0

outputData = open(dataPath+outputFileName,"w")
outputData.write("UserName|Tweet|Sentiment\n")

inputData = open(dataPath+inputFileName,"r")
for lines in inputData:
    tweet = lines.split("-->")[1]
    cleanTweet = re.sub('[^a-zA-Z0-9-_*\s#]', '', tweet)
    user = lines.split("-->")[0]
    myText = cleanTweet
    response = alchemyapi.sentiment("text", myText)
    try:
        outputData.write(user.strip("\s")+"|"+tweet.strip("\n")+"|"+response["docSentiment"]["type"]+"\n")
    except:
        print 'error'
inputData.close() 
outputData.close()   