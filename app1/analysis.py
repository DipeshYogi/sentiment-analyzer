import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords, wordnet
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_wordnet_pos(pos_tag):
  if pos_tag.startswith('J'):
    return wordnet.ADJ
  elif pos_tag.startswith('V'):
    return wordnet.VERB
  elif pos_tag.startswith('N'):
    return wordnet.NOUN
  elif pos_tag.startswith('R'):
    return wordnet.ADV
  else:
    return wordnet.NOUN

def analyseText(txt):
    txt = txt.lower()
    txt = [word.strip(string.punctuation) for word in txt.split(' ')]
    stop_words = set(stopwords.words('english'))

    txt = [x for x in txt if x not in stop_words]
    txt = [x for x in txt if len(x)>0]

    pos_tags = pos_tag(txt)
    txt = [WordNetLemmatizer().lemmatize(t[0],get_wordnet_pos(t[1])) for t in pos_tags]
    txt = ' '.join(txt)

    sid = SentimentIntensityAnalyzer()

    score = sid.polarity_scores(txt)
    print (score)

    return score
