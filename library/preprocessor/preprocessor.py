import pandas as pd

class PreProcessor:
 def __init__(self, df: pd.DataFrame):
    self.df = df

 def clean(self, subset: list):
    self.clean = self.df.dropna(subset = subset)

 def mean_na(self, df: pd.DataFrame):
    self.fill = self.df.fillna(self.df.mean())
