#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple feature that gives the number of tweets a user made in the given time period (depents on data set).

Created on Mon Oct 11 14:40:33 2021

@author: jnaether
"""

import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of hashtags in a tweet as a feature
class TweetTotalCount(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_tweet_total_count".format(input_column))
    
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # get values and reshape it in numpy array
    def _get_values(self, inputs):
               
        total_count = np.zeros((len(inputs[0]),1))
        
        for i in range(len(inputs[0])):
            total_count[i][0] = inputs[0][i]

        return total_count