import pandas as pd

class Load:
    def __init__(self, data: str):
        self.df = pd.read_csv(data)
        self.df = self.df.copy()
