#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:15:12 2021

@author: ml
"""

import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor
import pandas as pd


# class for extracting the number of hashtags in a tweet as a feature
class Year(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_year".format(input_column))
    
    
    def _get_values(self, inputs):

        year_array = np.zeros((len(inputs[0]),1)) 
        counter = 0
        for year in inputs[0]:
           year_array[counter] = year[0:4]
           counter+=1

        return year_array
    
class Month(FeatureExtractor):
   
    
   # constructor
   def __init__(self, input_column):
       super().__init__([input_column], "{0}_month".format(input_column))
   
   
   def _get_values(self, inputs):

       month_array = np.zeros((len(inputs[0]),1)) 
       counter = 0
       for month in inputs[0]:
          month_array[counter] = month[5:7]
          counter+=1
         
          return month_array
    
class Day(FeatureExtractor):
   
    
   # constructor
   def __init__(self, input_column):
       super().__init__([input_column], "{0}_day".format(input_column))
   
   
   def _get_values(self, inputs):

       day_array = np.zeros((len(inputs[0]),1)) 
       counter = 0
       for day in inputs[0]:
          day_array[counter] = day[8:10]
          counter+=1
       
       return day_array
    
class Weekday(FeatureExtractor):
    
    
    #constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_weekday".format(input_column))
                         
        
    def _get_values(self, inputs):
        
        
        weekday_array = np.zeros((len(inputs[0]),1))
        counter = 0
        for weekday in inputs[0]:
            temp = pd.Timestamp(weekday)
            weekday_array[counter] = temp.dayofweek
            counter+=1
        
        return weekday_array
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                         
                        