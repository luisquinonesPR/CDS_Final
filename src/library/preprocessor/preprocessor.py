import pandas as pd

class PreProcessor:
 def __init__(self, df: pd.DataFrame):
    self.df = df

 def clean(self, subset: list):
    self.clean = self.df.dropna(subset = subset)

 def mean_na(self, df: pd.DataFrame):
    self.fill = self.df.fillna(self.df.mean())

 def conditional_means(self, df: pd.DataFrame, subset: list):
    self.means = df.groupby('flight')[subset].mean()
    for column in self.means:
        df[column] = df.apply(lambda x: self.means[x.flight] if pd.isnull(x[column]) else x[column], axis=1)
    self.fill_means = df

 def conditional_modes(self, df: pd.DataFrame, subset: list):
    self.modes = df.groupby('flight')[subset].agg(pd.Series.mode)
    for column in self.modes:
        df[column] = df.apply(lambda x: self.modes[x.flight] if pd.isnull(x[column]) else x[column], axis=1)
    self.fill_modes = df
