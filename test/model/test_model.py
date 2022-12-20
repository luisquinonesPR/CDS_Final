# test Model   
        
import unittest

from library.model.model import Model

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE



class TestModel(unittest.TestCase):
    
   def test_predict_type(self):
        data = {'Col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                'Col2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                'Tar': [10, 18, 24, 28, 30, 30, 28, 24, 18, 10]}
        
        df_input = pd.DataFrame(data) 
        
        target = 'Tar'
        features = df_input.columns[df_input.columns != target]       
        X = df_input.loc[:, features]
        y = df_input.loc[:, [target]]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=3)
        
        input_model = Model(X_train, y_train)
        input_model.train_rf()
        output = input_model.predict(X_train)
        
        self.assertIsInstance(output, np.ndarray)

