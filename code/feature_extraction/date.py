#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:15:12 2021

@author: ml
"""

import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of hashtags in a tweet as a feature
class Year(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_year".format(input_column))
    
    
    def _get_values(self, inputs):
       
        #TODO one-hot-encoded
        #TODO SLICE ARRAY OF FORMAT
        #2020-05-10; YEAR-MONTH-DAY
        year_array = np.zeros((len(inputs[0]),1)) 
        counter = 0
        for year in inputs[0]:
           year_array[counter] = year[0:4]
           counter+=1
        print(year_array)
        
        
        return year_array
    
    
class Month(FeatureExtractor):
   
    
   # constructor
   def __init__(self, input_column):
       super().__init__([input_column], "{0}_month".format(input_column))
   
   
   def _get_values(self, inputs):
      
       #TODO one-hot-encoded
       #TODO SLICE ARRAY OF FORMAT
       #2020-05-10; YEAR-MONTH-DAY
       
       month_array = np.zeros((len(inputs[0]),1)) 
       counter = 0
       for month in inputs[0]:
          month_array[counter] = month[5:7]
          counter+=1
       print(month_array)
       
       
       return month_array
    
# TODO need to look up the weekday in some package of date probably.
class WeekDay(FeatureExtractor):
   
    
   # constructor
   def __init__(self, input_column):
       super().__init__([input_column], "{0}_month".format(input_column))
   
   
   def _get_values(self, inputs):
      
       #TODO one-hot-encoded
       #TODO SLICE ARRAY OF FORMAT
       #2020-05-10; YEAR-MONTH-DAY
       
       month_array = np.zeros((len(inputs[0]),1)) 
       counter = 0
       for month in inputs[0]:
          month_array[counter] = month[5:7]
          counter+=1
       print(month_array)
       
       
       return month_array
    