#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:01:20 2021

@author: Hendrik Timm
"""

# plotting with matplotlib
import pickle
from matplotlib import pyplot as plt
import numpy as np

show = 'TOTAL'
show = 'PERCENTAGE'


## TODO: Write own data_analysis graph with methods for percentage of viral tweets w.r.t. something and total number.

with open("data/feature_extraction/training.pickle", "rb") as f_in:
    data = pickle.load(f_in)

features = data["features"]
# only take the hashtag feature - probably some keyword is usable, but don't know how to access it right now.
features = features[:, 1:2]
labels = data["labels"]

pos = features[labels]
neg_index = np.array([not x for x in labels])
neg = features[neg_index]


bins = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

# plot Number of tweets w.r.t. number of hashtags
if(show=='TOTAL'):
    # total number of tweets
    plt.hist(features, bins = bins, color='blue',label=" all labels")
    plt.hist(neg, bins = bins, color='red', label="negative labels")
    plt.hist(pos, bins = bins, color='green', label= "positive labels", )
    plt.legend()
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Number of Tweets")


# plot percentage of viral tweets w.r.t. njmber of hashtags
elif(show=='PERCENTAGE'):
    viral_tweets = np.zeros((30,1))
    line = np.ones((30,1))
    for i in range(30):
        line[i][0] = 0.1
        viral = np.count_nonzero(pos == i)
        lame = np.count_nonzero(neg == i)
        if(viral+lame>0):
            viral_tweets[i][0] = viral/(lame+viral)
        
    plt.plot(viral_tweets, label='percent of viral tweets')
    plt.plot(line, color = 'red', label = "threshold")
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Percentage of viral tweets")
    plt.legend()
    
     
