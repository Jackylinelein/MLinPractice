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

with open("data/feature_extraction/training.pickle", "rb") as f_in:
    data = pickle.load(f_in)


num_hashtags = np.zeros((len(data["labels"]),1))

for i in range(len(data["features"][0])):
    num_hashtags[i][0] = data["features"][0][i].count(",")
    
    if(len(data["features"][0][i])>2):
        num_hashtags[i][0] +=1
   

features = num_hashtags
labels = data["labels"]


pos = features[labels]
neg_index = np.array([not x for x in labels])
neg = features[neg_index]


bins = [-1,0, 1,2,3,4,5,6,7,8,9,10]




    
plt.hist(features, bins = bins, color='blue',label=" all labels")

plt.hist(neg, bins = bins, color='red', label="negative labels")

plt.hist(pos, bins = bins, color='green', label= "positive labels", )

plt.legend()

plt.xlabel("Number of Hashtags")
plt.ylabel("Number of Tweets")
# count the specific numbers of positive/negative label for different #hashtags, here for example for 0 hashtags.
print(np.count_nonzero(pos == 0))
print(np.count_nonzero(neg == 0))