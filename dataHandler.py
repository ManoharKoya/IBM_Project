import os
import nltk
import csv
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
StopWds = set(stopwords.words("english"))


ct=0
tp=0
tpa=0 
tpc=0
percentage = 0.0
queryTxt = input()

def check(protxt):
    global ct,tp,tpa,tpc,percentage
    processed = nltk.word_tokenize(protxt)
    processedStr = [w for w in processed if w not in StopWds]
    processedStr = [ps.stem(w) for w in processedStr]
    lines = open("processedData.txt").read().splitlines()
    for line in lines:
        tp=0
        tpa=0
        prs = nltk.word_tokenize(line)
        for w in prs:
            if w in processedStr :  tp+=1
            tpa+=1
        perc = (float)(tp/tpa)
        ct+=1
        if perc>percentage: 
            tpc=ct
            percentage=perc
    print(percentage) 
    print(tpc)
    
check(queryTxt)
        
        



