#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import nltk
import sqlite3
import csv
from queryInfo import QueryInfo


conn = sqlite3.connect('example.db')
cur = conn.cursor()
# cur.execute("""create table infoData 
#             (title text,
#             view_ct integer,
#             ans_ct integer,
#             fav_ct integer,
#             tags text)""")

def retTags(Title):   
    A=-1  
    words = nltk.word_tokenize(Title)    # words should be proper nouns
    taggedP = nltk.pos_tag(words)
    Realtags = []
    for (a,b) in taggedP:
        if(b=='NNP') : 
            Realtags.append(a)
            A=0
    if(A==-1): 
        for (a,b) in taggedP:
            if(b=='NN'): 
                Realtags.append(a)
                A=0
    st = " "
    return st.join(Realtags)

def pushObj(obj,tags):
    t = (obj.title,obj.ViewCt,obj.AnsCt,obj.FavCt,tags)
    cur.execute("insert into infoData values (?,?,?,?,?)",t)
    

# with open("ShapeData-50K.csv",'r',encoding='utf-8') as csvFile:
#     reader = csv.reader(csvFile)
#     for [a,b,c,d,e] in reader:
#         obj = QueryInfo(b,c,d,e)
#         tags = retTags(b)
#         # print(tags)
#         pushObj(obj,tags)
        




cur.execute("""
                select * from infoData where ans_ct=50
            """)

print(cur.fetchall())
conn.commit()
conn.close()
