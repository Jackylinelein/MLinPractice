#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:01:34 2021

@author: jnaether
"""

import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of hashtags in a tweet as a feature
class WantedStr(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column, wanted_str):
        super().__init__([input_column], "{0}_wanted_str".format(input_column))
        self._wanted_str = wanted_str.lower()
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # get values and reshape it in numpy array
    def _get_values(self, inputs):
               
        wanted_str_list = np.zeros((len(inputs[0]),1))
        
        for i in range(len(inputs[0])):
            tweet = inputs[0][i]
            if self._wanted_str in tweet.lower():
                wanted_str_list[i][0] = True
            else:
                wanted_str_list[i][0] = False

        return wanted_str_list
    