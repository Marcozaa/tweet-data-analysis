
import numpy as np
import pandas as pd
import nltk
nltk.download('vader_lexicon')
import re
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer





df = pd.read_csv('russia.csv')
df.set_index("date", inplace=True)





for tweet in df["tweet"]:
    sid = SentimentIntensityAnalyzer()
    print(tweet)
    ss = sid.polarity_scores(tweet)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()


