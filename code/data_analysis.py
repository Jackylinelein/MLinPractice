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

features = data["hashtags"]
labels = data["labels"]

# plt.hist(features)
plt.hist(features, range = [0,400])

pos = features[labels]
neg_index = np.array([not x for x in labels])
neg = features[neg_index]

