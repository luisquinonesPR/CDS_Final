import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

class Model:
    def __init__(self, feat_cols: pd.DataFrame, targ_col: pd.Series):
        self.__feat_cols_ = feat_cols
        self.__targ_col_ = targ_col
        lab = LabelEncoder()
        self.__targ_col_ = lab.fit_transform(self.__targ_col_)

    def train_rf(self):
        model_ = RandomForestRegressor(max_depth=5)
        self.fit = model_.fit(self.__feat_cols_, self.__targ_col_)

    def predict(self, data: pd.DataFrame):
        self.data = data
        self.predict_ = self.fit.predict(self.data)
        return self.predict_
