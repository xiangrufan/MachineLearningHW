import numpy as np

S = ['S']
M = ['M']
L = ['L']
n = [-1]
p = [1]
X_train = [1]*5 + [2]*5 +[3]*5
X2_train = S + M*2 +S*3 + M*2 + L*3 + M*2 + L*2
Y_train= n*2 + p*2 +n*3 +p*7 +n



Y_type = n + p
X1_type = [1,2,3]
X2_type = S + M + L

X_train, X2_train, Y_train = [np.array(tmp) for tmp in [X_train, X2_train,Y_train]]
P_Y_ck = np.array( [ sum(Y_train==type)/Y_train.shape[0] for type in [-1,1]])
P_Y_ck /= 2
# X1, X2 is not related.
# Y and X1, X2 are related, forms a coefficient matrix
P_X1_giv_Y = np.zeros((len(X1_type),len(Y_type)))
P_X2_giv_Y = np.zeros((len(X2_type),len(Y_type)))
P_Y = np.zeros(len(Y_type))
# for idx,y in enumerate(Y_type):
#     for idj, x in enumerate(X1_type):
#         pass
for id in range (len(X_train)):
        type = Y_train[id]
        type_id = Y_type.index(type)
        X1 = X_train[id]
        X1_id = X1_type.index(X1)
        X2 = X2_train[id]
        X2_id = X2_type.index(X2)
        P_X1_giv_Y[X1_id, type_id] += 1
        P_X2_giv_Y[X2_id, type_id] += 1
        P_Y[type_id] += 1

# sum_events = np.sum(P_Y) = len(X_train)
P_X1_giv_Y = P_X1_giv_Y/P_Y # sum_events cancel each other
P_X2_giv_Y = P_X2_giv_Y/P_Y
P_Y = P_Y/np.sum(P_Y)

x_test = [2,'S']
X1_id = X1_type.index(x_test[0])
X2_id = X2_type.index(x_test[1])
# computed the preducted P(Y|X)
P_Y_giv_X  = P_Y*P_X1_giv_Y[X1_id]*P_X2_giv_Y[X2_id]

#
# for jtype in [X_train,X2_train]:
#     for ltype in feature_dict['x']:
#         P_X_ajl_given_Y_ck = [ sum(Y_train==type)/Y_train.shape[0] for type in S+M+L ]
