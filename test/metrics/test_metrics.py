import unittest

from sklearn.metrics import mean_squared_error
from library.metrics.metrics import Metrics
import numpy as np

class Test_Metrics(unittest.TestCase):

    def test_Mse(self):
        y_test= np.random.rand(1,10)
        y_pred= np.random.rand(1,10)
        expected_output = mean_squared_error(y_test, y_pred)
        output = Metrics.mse(y_test, y_pred)
        self.assertEqual(expected_output, output)

