#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Counts how often a element is present in the list.

@author: jnaether
"""

from code.preprocessing.preprocessor import Preprocessor

class Counter(Preprocessor):
    """Count the total number of occurs of each element of the given column"""
    
    def __init__(self, input_column, output_column):
        """Initialize the Counter with the given input and output column."""
        super().__init__([input_column], output_column)
    
    # don't need to implement _set_variables(), since no variables to set
    
    def _get_values(self, inputs):
        """Count total number of elements in input list."""
        
        total_count = []
        
        # convert to normal list, so that the count function can be used
        input_list = inputs[0].values.tolist()
        
        for element in input_list:
            total_count.append(input_list.count(element))           
            
        return total_count