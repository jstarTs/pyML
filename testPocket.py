import numpy as np
import random

input = np.loadtxt('./hw1_18_train.dat')

x0 = 1

# Pocket algo.
# random cyclic
# training
eta = 1
updatetime = 0
runtime = 0
mistakeAll = 0
mistakeAvg = 0
R_mistake = 0
rw0, rw1, rw2, rw3, rw4 = 0, 0, 0, 0, 0
for i in range(0,1):
    x = set()
    mistake = 0
    w0, w1, w2, w3, w4 = 0, 0, 0, 0, 0
    while((updatetime <= 100) and (runtime<=2000)):

        # randomNum = random.randrange(0,500)
        randomNum = random.randint(0,499)
        runtime= runtime + 1
        # input 變數 , x0例外
        x1, x2, x3, x4 = input[randomNum,0:4].astype('float')
        print(input[randomNum,0:4])
        sum = x0 * w0 + x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4

        if sum > 0:
            g = 1
        else:
            g = -1

        print('g:' +str(g) + ' , ig:' + str(input[randomNum,4]))
        if g != input[randomNum,4]:
            # ▵w = y*x * eta
            # w = w + ▵w
            w0 = w0 + x0 * input[randomNum,4] * eta
            w1 = w1 + x1 * input[randomNum,4] * eta
            w2 = w2 + x2 * input[randomNum,4] * eta
            w3 = w3 + x3 * input[randomNum,4] * eta
            w4 = w4 + x4 * input[randomNum,4] * eta

            mistake = 0
            for i in input:
                x1, x2, x3, x4 = i[0:4].astype('float')
                sum = x0 * w0 + x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4

                if sum > 0:
                    g = 1
                else:
                    g = -1

                if g != i[4]:
                    mistake = mistake + 1


            if(R_mistake>mistake)or(updatetime==0):
                # if R_mistake != 0:
                updatetime = updatetime + 1
                R_mistake = mistake
                rw0, rw1, rw2, rw3, rw4 = w0, w1, w2, w3, w4

        print(str(updatetime)+ ' , R:'+ str(R_mistake)+ ' , r:'+ str(mistake))


    # pocket
    # if i == 0:
    #     R_mistake = mistake
    #     rw0, rw1, rw2, rw3, rw4 = w0, w1, w2, w3, w4
    # elif mistake < R_mistake:
    #     R_mistake = mistake
    #     rw0, rw1, rw2, rw3, rw4 = w0, w1, w2, w3, w4

    # print(mistake)
    # mistakeAll = mistakeAll + mistake

# mistakeAvg = mistakeAll / 2000
# print(mistakeAvg)

print('--------')

input = np.loadtxt('./hw1_18_test.dat')
# Pocket algo.
# random cyclic
# test
eta = 1
mistakeAll = 0
mistakeAvg = 0
R_mistake = 0

for i in range(0,2000):
    w0, w1, w2, w3, w4 = rw0, rw1, rw2, rw3, rw4

    randomNum = random.randint(0, 499)
    x1, x2, x3, x4 = input[randomNum,0:4].astype('float')
    sum = x0 * w0 + x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4

    if sum > 0:
        g = 1
    else:
        g = -1

    if g != input[randomNum, 4]:
        mistake = mistake + 1


mistakeAvg = mistake / 2000
print(mistakeAvg)
