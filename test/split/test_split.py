# test split

import unittest

from library.split.split import Split

import pandas as pd
from sklearn.model_selection import train_test_split
from pandas.testing import assert_frame_equal

class TestSplit(unittest.TestCase):
    
    def test_split(self):        
        data = {'Col1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
                'Col2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        df_input = pd.DataFrame(data)
        df_output = Split(df_input)
        test_output = df_output.test
        train_output = df_output.train

        expected_output = 2 #or whatever fraction of 10 we end up defining as the test
        self.assertEqual(len(test_output), expected_output)
