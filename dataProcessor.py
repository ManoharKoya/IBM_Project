import nltk
import csv
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
StopWds = set(stopwords.words("english"))

def processor(protxt):
    processed = nltk.word_tokenize(protxt)
    processedStr = [w for w in processed if w not in StopWds]
    processedStr = [ps.stem(w) for w in processedStr]
    f = open("processedData.txt",'a', encoding="utf8")
    for w in processedStr:
        f.write(w) 
        f.write(" ")
    f.write("\n")
    f.close()
with open('QueryResults-50K.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for [a,b,c] in reader :
        processor(b)
        
    