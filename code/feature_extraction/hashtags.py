#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:19:47 2021

@author: Hendrik Timm
"""


import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of hashtags in a tweet as a feature
class Hashtags(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_#hashtags".format(input_column))
    
    
    def _get_values(self, inputs):
       
       
        num_hashtags = np.zeros((len(inputs[0]),1)) 
        for i in range(len(inputs[0])):
            
            num_hashtags[i][0] = inputs[0][i].count(",")
            
            if(len(inputs[0][i])>2):
                num_hashtags[i][0] +=1
                  
        return num_hashtags