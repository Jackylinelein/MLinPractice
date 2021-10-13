#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:12:18 2021

@author: jnaether
"""


import unittest
import pandas as pd
from code.feature_extraction.wanted_str import WantedStr

class WantedStrTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = ["This is a test tweet"]
        
        self.wanted_str_true = "test"
        self.wanted_str_feature_true = WantedStr(self.INPUT_COLUMN, self.wanted_str_true)
        
        self.wanted_str_capital = "Test"
        self.wanted_str_feature_capital = WantedStr(self.INPUT_COLUMN, self.wanted_str_capital)
        
        self.wanted_str_lower = "this"
        self.wanted_str_feature_lower = WantedStr(self.INPUT_COLUMN, self.wanted_str_lower)
        
        self.wanted_str_false = "not inside string"
        self.wanted_str_feature_false = WantedStr(self.INPUT_COLUMN, self.wanted_str_false)
        
     
    def test_input_columns(self):
        self.assertEqual(self.wanted_str_feature_true._input_columns, [self.INPUT_COLUMN])


    def test_feature_name(self):
        self.assertEqual(self.wanted_str_feature_true.get_feature_name(), self.INPUT_COLUMN + "_wanted_str")


    def test_list_of_wanted_str_true(self):
        EXPECTED_ANSWER = True
        self.assertEqual(self.wanted_str_feature_true.transform(self.df), EXPECTED_ANSWER)


    def test_list_of_wanted_str_false(self):
        EXPECTED_ANSWER = False
        self.assertEqual(self.wanted_str_feature_false.transform(self.df), EXPECTED_ANSWER)
        
        
    def test_list_of_wanted_str_capital(self):
        EXPECTED_ANSWER = True
        self.assertEqual(self.wanted_str_feature_capital.transform(self.df), EXPECTED_ANSWER)
        

    def test_list_of_wanted_str_lower(self):
        EXPECTED_ANSWER = True
        self.assertEqual(self.wanted_str_feature_lower.transform(self.df), EXPECTED_ANSWER)
        
        
if __name__ == '__main__':
    unittest.main()