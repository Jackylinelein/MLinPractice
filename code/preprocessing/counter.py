#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Counts how often a element is present in the list.

@author: jnaether, htimm
"""

import numpy as np
from code.preprocessing.preprocessor import Preprocessor

class Counter(Preprocessor):
    """Count the total number of occurs of each element of the given column"""
    
    def __init__(self, input_column, output_column):
        """Initialize the Counter with the given input and output column."""
        super().__init__([input_column], output_column)
    
    # don't need to implement _set_variables(), since no variables to set

    def _get_values(self, inputs):
        """Count total number of elements in input list."""
     
        user_dict = {}
        total_count= np.zeros((len(inputs[0]),1)) 
        
        for user_name in inputs[0]:
            if(user_name not in user_dict):
                user_dict[user_name] = 1
            else:
                user_dict[user_name] = user_dict[user_name]+ 1
                
        counter = 0
        for user_name in inputs[0]:
            total_count[counter] = user_dict[user_name]
            counter+=1
                 
        return total_count

    
        