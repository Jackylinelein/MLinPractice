#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:28:14 2021

@author: jnaether
"""

import unittest
import pandas as pd
from code.preprocessing.counter import Counter

class CounterTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN ="input"
        self.OUTPUT_COLUMN = "output"
        self.counter = Counter(self.INPUT_COLUMN, self.OUTPUT_COLUMN)
        
        
    def test_input_columns(self):
        self.assertListEqual(self.counter._input_columns, [self.INPUT_COLUMN])

    def test_output_columns(self):
        self.assertEqual(self.counter._output_column, self.OUTPUT_COLUMN)

    def test_counting(self):
        input_name = ["element1","element2","element1","element1","element3"]
        output_count = 3
        
        input_df = pd.DataFrame()
        input_df[self.INPUT_COLUMN] = input_name
        
        counted = self.counter.fit_transform(input_df)
        self.assertEqual(counted[self.OUTPUT_COLUMN][0], output_count)


# needed to run script using the spyder console
if __name__ == '__main__':
    unittest.main()
