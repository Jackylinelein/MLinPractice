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
#print(list(data["features"]))
print(data["features"][0][0])
print((data["features"][0][0]).count(",")+1)

print(data["features"][0][1])
print(len(data["features"][0][1]))


#TODO:
    # insert number of hashtags of each entry in a new array of the same size as the labels/overall tweets.
    # graphically see if there is any difference

num_hashtags = np.zeros(len(data["labels"]))
print(len(data["labels"]))
print(len(num_hashtags))

for hashtags in data["features"][0]:
    pass


#print(data["labels"][100])

features = data["features"]
labels = data["labels"]
print(features)

# plt.hist(features)
#plt.hist(features, range = [0,400])

pos = features[labels]
neg_index = np.array([not x for x in labels])
neg = features[neg_index]

