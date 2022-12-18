# test preprocessor   
        
import unittest

from library.preprocessor.preprocessor import PreProcessor

import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from sklearn.model_selection import train_test_split


class TestPreProcessor(unittest.TestCase):
    
    def test_preprocessor_remove(self):        
        data = {'Col1': [np.nan, 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
                'Col2': [0, 1, 1, 1, 1, 3, 3, 3, 3, np.nan]}
        df_input = pd.DataFrame(data)        
        df_output = PreProcessor(df_input)
        df_output.clean(['Col1', 'Col2])
        df_output = df_output.clean
        
        output = df_output.isna().sum().sum()
        expected_output = 0 #not more nan values in any columns
       
        self.assertEqual(output, expected_output)
        
     def test_preprocessor_fill(self):        
        data = {'Col1': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'a'],
                'Col2': [1, 1, 3, 3, 5, 5, 7, 7, np.nan, np.nan]} #means: a-2, b-6, all-4 
        df_input = pd.DataFrame(data)        
        df_output = PreProcessor(df_input)
        df_output.mean_na(df_output.df['Col2']
        df_output = df_output.clean
        
        output = df_output['Col2'].iat[-1]
        expected_output = 4
        
        self.assertEqual(output, expected_output)
        
     #def test_preprocessor_cond_fill(self):

     #def test_preprocessor_mode_fill(self): 
