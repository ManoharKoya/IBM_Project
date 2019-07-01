import os
import pandas as pd
import nltk
import gensim
from gensim import corpora, models, similarities

f = open("reviews_data.txt",'r',encoding='utf8')
txt = f.read()

tok_corp = [nltk.word_tokenize(txt)]

model = gensim.models.Word2Vec(tok_corp,min_count=1,size=32)

print(txt)
