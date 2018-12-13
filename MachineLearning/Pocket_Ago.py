"""
Pocket Algorithm
Modify PLA
"""

import numpy as np

class Pocket_Algo:

    def __init__(self, InData):
        # Input data set
        self.InData = InData


    """
        Y = WX
        X_variavle : ndarray,設定X(vector)變數
        W_coefficient : ndarray,設定Ｗ(vector)係數

        return -> g : discriminating result
        """

    def pla_process(self, X_variavle, W_coefficient):
        sum = X_variavle * W_coefficient

        if sum > 0:
            # g = 1
            return 1
        else:
            # g = -1
            return -1
        # return g


    """
    Y = WX
    X_variavle : ndarray,設定X(vector)變數
    W_coefficient : ndarray,設定Ｗ(vector)係數
    Y_label : 
    gy : 分類結果
    Eta : 

    return -> g : discriminating result
    """
    def pla_error(self, X_variavle, W_coefficient, Y_label, gy, Eta=1):
        if gy == Y_label:
            return True
        else:
            return W_coefficient + X_variavle * Y_label * Eta

