# test Model   
        
import unittest

from library.model.model import Model

import pandas as pd
from pandas.testing import assert_frame_equal
from sklearn.datasets import load_iris
from sklearn.utils import check_random_state
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder


#class TestModel(unittest.TestCase):
    
#   def test_train(self):
#        iris = load_iris()
#        #not sure what value this permutation is adding - it's just changing the order 
#        rng = check_random_state(1)
#        perm = rng.permutation(iris.target.size)
#        iris.data =  iris.data[perm]
#        iris.target = iris.target[perm]
#        
#        input_model = Model(iris.data, iris.target)
#        input_model.train(reg = "l2")
#        
#        output_prediction = model.predict(iris.data)
#        expected_output =  iris.target
#
#        self.assertEqual(output, expected_output)
        
