#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:19:47 2021

@author: Hendrik Timm
"""


import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the character-based length as a feature
class Hashtags(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_charlength".format(input_column))
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # compute the number of hashtags based on the inputs (every hashtag in a list)
    def _get_values(self, inputs):
       
        #create an np array to store the number of hashtags, initialize with 0's
        num_hashtags = np.zeros((len(inputs[0]),1))
        
        # go through all the inputs (which are lists with all the hashtags in it)
        for i in range(len(inputs[0])):
            # count how many hashtags are in there with a little workaround: simple count ","
            # with 0 "," -> 0 or 1 hashtags, with 1 "," -> 2 hashtags, so
            num_hashtags[i][0] = inputs[0][i].count(",")
            
            # if the length > 2: it means it does not only contain an empty "[]" but something
            # in it -> at least 1 hashtag, add one hashtag number to current tweet
            if(len(inputs[0][i])>2):
                num_hashtags[i][0] +=1
            
        # return created array
        return num_hashtags