import pandas as pd
from sklearn.model_selection import train_test_split

class Split:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.train, self.test = train_test_split(self.df, test_size=0.5)