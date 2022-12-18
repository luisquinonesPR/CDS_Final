import unittest

import pandas as pd
import numpy as np
from library.features.features import Polynomial, Standardize, One_Hot_Enc
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from pandas.testing import assert_frame_equal

class Test_Standardize(unittest.TestCase):

    def test_Transform(self):
        test_df = pd.DataFrame(np.random.randint(100, size=(5,4)))
        scaled_df = StandardScaler().fit_transform(test_df)
        expected_output=pd.DataFrame(scaled_df, columns = test_df.columns, index = test_df.index)
        scaler = Standardize(test_df)
        output = scaler.transform()
        assert_frame_equal(expected_output, output, check_dtype=False)
        
class Test_Polynomial(unittest.TestCase):
    
    def test_Transform(self):
        test_df = pd.DataFrame(np.random.randint(100, size=(5,4)))
        test_df.columns = ["c1", "c2", "c3", "c4"]
        poly=PolynomialFeatures(2)
        poly_df = poly.fit_transform(test_df)
        poly_cols=poly.get_feature_names_out(test_df.columns)
        expected_output = pd.DataFrame(poly_df, columns = poly_cols, index = test_df.index)
        output = Polynomial(test_df)
        output = output.transform(2)
        assert_frame_equal(expected_output, output, check_dtype=False)
        

class Test_One_Hot_Enc(unittest.TestCase):
    
    def test_Transform(self):
        
        data = {'product_name': ['laptop', 'printer', 'tablet', 'desk', 'chair'],
        'price': [1200, 150, 300, 450, 200],
        'model':[1000, 400, 1000, 200, 100]
        }
        test_df = pd.DataFrame(data)
        expected_output = pd.get_dummies(test_df, drop_first=False)
        output = One_Hot_Enc(test_df).transform()
        assert_frame_equal(expected_output, output, check_dtype=False)


        
    
    
        



