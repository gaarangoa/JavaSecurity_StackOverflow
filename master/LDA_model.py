__author__ = 'wujunyan'
import json

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from nltk.stem.porter import PorterStemmer
import gensim
import sys


ff = open("Q_and_A.json")
v2 = json.load(ff)

lq = dict()
for i in xrange(len(v2)):
#for i in xrange(500):
   lq[v2[i]['link']]=v2[i]['question']+' '.join(v2[i]['answers'])

all_v2=[]
for i in lq.keys():
  all_v2.append(lq[i])

all_v22=filter(None, all_v2)
texts=[]

### tools
en_stop = get_stop_words('en')
tokenizer = RegexpTokenizer(r'\w+')
p_stemmer = PorterStemmer()

### parsing
for i in all_v22:
  raw = i.lower()
  tokens = tokenizer.tokenize(raw)
  stopped_tokens = [i for i in tokens if not i in en_stop]
  clean_tokens = [i for i in stopped_tokens if i.isalpha()]
  stemed = [p_stemmer.stem(i) for i in stopped_tokens]
  texts.append([i for i in stemed])

dictionary = corpora.Dictionary(texts)

### training
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=25, id2word = dictionary, passes=20)

### print the topic
for i in xrange(25):
   print(ldamodel.print_topics(num_topics=25, num_words=30)[i])

### applying the model
linkSet = lq.keys()
sys.stdout.write('.')
tt = dict()

for i in linkSet:
    print i,
    raw = lq[i].lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    clean_tokens = [i for i in stopped_tokens if i.isalpha()]
    stemed = [p_stemmer.stem(i) for i in stopped_tokens]
    vector = dictionary.doc2bow(stemed)
    doc_lda = ldamodel[vector]
    tt = dict()
    for j in xrange(len(doc_lda)):
        tt[doc_lda[j][0]]=doc_lda[j][1]
    for k in xrange(1,31):
        try:
            #print "\t%f" %(tt[k])
            if tt[k]>=0.1:
                print "\t%f" %(tt[k]),
            else:
                print "\t0",
        except:
            print "\t0",
    print 






