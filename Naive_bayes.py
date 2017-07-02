import numpy as np
x_test = [2,'S']
S = ['S']
M = ['M']
L = ['L']
n = [-1]
p = [1]
X_train = [1]*5 + [2]*5 +[3]*5
X2_train = S + M*2 +S*3 + M*2 + L*3 + M*2 + L*2
Y_train= n*2 + p*2 +n*3 +p*7 +n
X_train, X2_train, Y_train = [np.array(tmp) for tmp in [X_train, X2_train,Y_train]]
P_Y_ck = [ sum(Y_train==type)/Y_train.shape[0] for type in [-1,1]]
P_Y_ck /= 2

for jtype in [X_train,X2_train]:
    for ltype in feature_dict['x']
P_X_ajl_given_Y_ck = [ sum(Y_train==type)/Y_train.shape[0] for type in S+M+L ]
