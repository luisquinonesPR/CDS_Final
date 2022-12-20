from sklearn.metrics import mean_squared_error

class Metrics:

    def mse(y_test, y_pred):
        score =  mean_squared_error(y_test, y_pred, squared=False)
        return score
