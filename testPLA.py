import numpy as np
import random

input = np.loadtxt('./hw1_15_train.dat')

# print(input)
# print(input[0 , 0:4])

# 係數初始化
w0, w1, w2, w3, w4 = 0, 0, 0, 0, 0
# x0變數初始化
x0 = 1

test = 0

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
    return W_coefficient + X_variavle*Y_label*Eta

# naive cyclic
for i in input:

    # input 變數 , x0例外
    x1, x2, x3, x4 = i[0:4].astype('float')
    sum = x0 * w0 + x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4

    if sum > 0:
        g = 1
    else:
        g = -1

    if g != i[4]:
        test = test + 1
        # ▵w = y*x
        # w = w + ▵w
        w0 = w0 + x0 * i[4]
        w1 = w1 + x1 * i[4]
        w2 = w2 + x2 * i[4]
        w3 = w3 + x3 * i[4]
        w4 = w4 + x4 * i[4]
    else:
        print(i)
        print(str(g)+','+str(i[4]))
        print(test)




# random cyclic
# updateTime = 0
# eta = 1
# for i in range(0,2000):
#     x = set()
#     test = 0
#     w0, w1, w2, w3, w4 = 0, 0, 0, 0, 0
#     while(1):
#         if len(x) >= 400:
#             break
#
#         # randomNum = random.randrange(0,400)
#         randomNum = random.randint(0,399)
#         if randomNum in x :
#             continue
#         else:
#            x.add(randomNum)
#         # input 變數 , x0例外
#         x1, x2, x3, x4 = input[randomNum,0:4].astype('float')
#         sum = x0 * w0 + x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4
#
#         if sum > 0:
#             g = 1
#         else:
#             g = -1
#
#         if g != input[randomNum,4]:
#             test = test + 1
#             # ▵w = y*x * eta
#             # w = w + ▵w
#             w0 = w0 + x0 * input[randomNum,4] * eta
#             w1 = w1 + x1 * input[randomNum,4] * eta
#             w2 = w2 + x2 * input[randomNum,4] * eta
#             w3 = w3 + x3 * input[randomNum,4] * eta
#             w4 = w4 + x4 * input[randomNum,4] * eta
#         # else:
#         #     print(test)
#
#     print(test)
#     updateTime = updateTime + test
#
# result = updateTime / 2000
# print(result)

