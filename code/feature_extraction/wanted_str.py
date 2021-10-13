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
        self._wanted_str = wanted_str
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # get values and reshape it in numpy array
    def _get_values(self, inputs):
               
        wanted_str_list = np.zeros((len(inputs[0]),1))
        
        for tweet in inputs[0]:
            
            if wanted_str in tweet:
                wanted_str_list.append(True)
            else:
                wanted_str_list.append(False)

        return wanted_str_list