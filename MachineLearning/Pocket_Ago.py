"""
Pocket Algorithm
Modify PLA
"""

import numpy as np

class Pocket_Algo:

    def a(self):
        pass

    """
        Y = WX
        X_variavle : ndarray,設定X(vector)變數
        W_coefficient : ndarray,設定Ｗ(vector)係數

        return -> g : discriminating result
        """

    def pla_process(X_variavle, W_coefficient):
        sum = X_variavle * W_coefficient

        if sum > 0:
            # g = 1
            return 1
        else:
            # g = -1
            return -1
        # return g

    """
    """

    def pla_discriminate(gy, Y):
        if gy == Y:
            return True
        else:
            return False

    """
    Y = WX
    X_variavle : ndarray,設定X(vector)變數
    W_coefficient : ndarray,設定Ｗ(vector)係數

    return -> g : discriminating result
    """

    def pla_update(X_variavle, W_coefficient, Y_label, Eta=1):
        # rW_coefficient = W_coefficient + X_variavle*Y_label*Eta
        return W_coefficient + X_variavle * Y_label * Eta


