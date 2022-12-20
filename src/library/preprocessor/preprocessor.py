import pandas as pd

class PreProcessor:
 def __init__(self, df: pd.DataFrame):
    self.df = df

 def clean(self, subset: list):
    self.clean = self.df.dropna(subset = subset)

 def mean_na(self, df: pd.DataFrame):
    self.fill = self.df.fillna(self.df.mean())

 def conditional_means(self, df: pd.DataFrame, subset: list):
    df[subset] = df[subset].fillna(df.groupby('flight', as_index=True)[subset].transform('mean'))
    self.fill_means = df

 def conditional_modes(self, df: pd.DataFrame, subset: list):
    df[subset] = df[subset].fillna(df.groupby('flight', as_index=True)[subset].transform(lambda S: S.mode()[0]))
    self.fill_modes = df
