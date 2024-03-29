#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import nltk
import sqlite3
import csv
from queryInfo import QueryInfo
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords


ps = PorterStemmer()
StopWds = set(stopwords.words("english"))


conn = sqlite3.connect('example.db')
cur = conn.cursor()

def createTable():
    cur.execute("""create table infoData 
            (title text,
            view_ct integer,
            ans_ct integer,
            fav_ct integer,
            tags text)""")

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

def pushObj(obj,tags):
    t = (obj.title,obj.ViewCt,obj.AnsCt,obj.FavCt,tags)
    cur.execute("insert into infoData values (?,?,?,?,?)",t)
    

createTable()

with open("ShapeData-50K.csv",'r',encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile)
        for [a,b,c,d,e] in reader:
            obj = QueryInfo(b,c,d,e)
            tags = retTags(b)
            # print(tags)
            pushObj(obj,tags)


# def csvToDB():
#     with open("ShapeData-50K.csv",'r',encoding='utf-8') as csvFile:
#         reader = csv.reader(csvFile)
#     for [a,b,c,d,e] in reader:
#         obj = QueryInfo(b,c,d,e)
#         tags = retTags(b)
#         # print(tags)
#         pushObj(obj,tags)


# cur.execute("""
#               select * from infoData where fav_ct=3
#             """)


# print(cur.fetchall())
conn.commit()
conn.close()
