import numpy as np
import random
import MachineLearning.Pocket_Ago as pocket

runtime=0
updatetime=0

# w0, w1, w2, w3, w4
W = np.asarray([0,0,0,0,0])
# rw0, rw1, rw2, rw3, rw4
rW = np.asarray([0,0,0,0,0])
r_mistake = 0
x = np.asarray([0])

while (updatetime<=100) and (runtime<=2000):
    # randomNum = random.randrange(0,500)
    randomNum = random.randint(0, 499)
    runtime = runtime + 1
    X =np.hstack(x, input[randomNum, 0:4])

    gy = pocket.pla_process(X,W)

    result = pocket.pla_error(X, W, input[randomNum,4], gy)
    if result != True:
        rW = result


