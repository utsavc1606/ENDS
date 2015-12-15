'''
Created on Dec 12, 2015

@author: utsavchatterjee
'''
import re
from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

outputFile = ("/Users/utsavchatterjee/Desktop/intermediate.txt", "w")
tid =  1;
tdict = {}
with open("/Users/utsavchatterjee/Documents/Python Projects/ENDS Tweet Analysis/ENDS/Data/testData.txt", "r") as inputfile :
    for lines in inputfile:
        tweets = lines.split("-->")[1].lstrip()
        tweets = re.sub("[^A-Za-z0-9#\s'.@]+", '', tweets)
        tdict[tid] = tweets.strip("\n")
        tid+=1

for k in tdict:
#     print tdict[k]
    response = alchemyapi.sentiment("text", str(tdict[k]))
    for x in response:
        print x+":"+response[x]
#     sentiment = response["docSentiment"]["type"]
    print response

# myText = "ecigitesztek --> Dressed in some festive  to  and celebrate with  tonight! See you soon   https:\/\/t.co\/4xGOubXC0O #vape #ecig"
# myText =  re.sub("[^A-Za-z0-9#\s'.]+", '', myText)
# response = alchemyapi.sentiment("text", myText)
# print response["docSentiment"]["type"]+"\n"
