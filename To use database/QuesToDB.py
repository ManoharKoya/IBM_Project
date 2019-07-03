import os
import nltk
import sqlite3
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


ps = PorterStemmer()
StopWds = set(stopwords.words("english"))

txt = input("Entering title: ")

def retTags(Title):   
    A=-1  
    wds = nltk.word_tokenize(Title)    # words should be proper nouns
    words = [w for w in wds if w not in StopWds]
    taggedP = nltk.pos_tag(words)
    Realtags = []
    for (a,b) in taggedP:
        if(b=='NNP' or b.startswith('VB') or b=="NN") : 
            Realtags.append(a)
            A=0
    rtags = [ps.stem(w) for w in Realtags]
    st = " "
    return st.join(rtags)

tags = retTags(txt)
conn = sqlite3.connect('example.db')
c = conn.cursor()
t = (txt,1,1,1,tags)
c.execute("""
          insert into infoData values(?,?,?,?,?)
          """, t)
conn.commit()
conn.close()
print("pushed into db")
