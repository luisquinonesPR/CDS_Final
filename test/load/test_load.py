import unittest

from library.load import load
import pandas as pd
from pandas.testing import assert_frame_equal


class Test_Load(unittest.TestCase):

    def test_Load(self):
        expected_output = pd.read_csv("Flights_Data.csv")
        output = load.Load('Flights_Data.csv')
        output = output.df
        assert_frame_equal(expected_output, output, check_dtype=False)



