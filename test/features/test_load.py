import unittest

from library.load.load import Load
import pandas as pd
from pandas.testing import assert_frame_equal


class Test_Load(unittest.TestCase):

    def test_Load(self):
        expected_output = pd.read_csv("Flights_Data.csv")
        output = Load('Flights_Data.csv')
        assert_frame_equal(output, expected_output)
        with self.assertRaises(FileNotFoundError):
            Load('whatever.csv')
