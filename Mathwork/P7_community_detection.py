import numpy as np
np.set_printoptions(threshold=np.inf)

def community_detection(data,index):
    col = row = data.max()
    col = int(col)
    data_matrix_pos = makeMatrix(row,col,data,1)
    data_matrix_neg = makeMatrix(row,col,data,-1)

    # +++、--+、++-、---
    PPP = np.dot(data_matrix_pos, data_matrix_pos) * data_matrix_pos
    NNP = np.dot(data_matrix_neg, data_matrix_neg) * data_matrix_pos
    PPN = np.dot(data_matrix_pos, data_matrix_pos) * data_matrix_neg
    NNN = np.dot(data_matrix_neg, data_matrix_neg) * data_matrix_neg

    #归一化
    SUM_denominator = PPP + NNP + PPN + NNN
    SUM = PPP+ NNP

    [x, y] = np.where(SUM_denominator == 0)
    SUM[x][y] = 0
    [x,y] = np.where(SUM_denominator != 0)
    for i in range(len(x)):
        SUM[x[i]][y[i]] = SUM[x[i]][y[i]] / SUM_denominator[x[i]][y[i]]

    #SUM中每个节点的度数
    Out_degree = np.zeros(shape=(1,col))

    Out_degree[0] = SUM.sum(axis=1)
    K = Out_degree;
    tot = Out_degree.sum()
    G = SUM - (np.dot(K.T,K)/(tot));
    if(index == 8):
        for i in range(int(row)):
            G[i][i] = 0 - SUM.sum(axis=1)[i]-G[i][i]

    #求特征值和特征向量
    [eigenvalues, eigenvectors] = np.linalg.eig(G)
    m = max(eigenvalues)
    for i in range(len(eigenvalues)):
        if eigenvalues[i] == m:
            max_eigenvector = eigenvectors[:,i]
            break

    #划分社团:list_A，list_B
    Set_A = [];Set_B = [];
    s = np.zeros(shape=(1,len(max_eigenvector)))
    for i in range(len(max_eigenvector)):
        if max_eigenvector[i] > 0:
            Set_A.append(i+1)
            s[0][i] = 1
        else:
            Set_B.append(i + 1)
            s[0][i] = -1
    Q = np.dot(np.dot(s,G),s.T)

    #去除

    data_A = Make_community(data, Set_A, Set_B)
    data_B = Make_community(data, Set_B, Set_A)

    data_A,dict_A,Set_A = Make_dictionary(data_A,Set_A)
    data_B,dict_B,Set_B = Make_dictionary(data_B,Set_B)

    return data_A, dict_A, Set_A, data_B, dict_B, Set_B







def makeMatrix(row,col,data,key):
    matrix = np.zeros(shape=(int(row),int(col)))
    for i in range(len(data)):
        if data[i][2] == key:
            matrix[int(data[i][0])-1][int(data[i][1])-1] = 1
    return matrix

def Make_community(data,list_A,list_B):
    res = np.array([[0,0,0]])
    for i in range(len(data)):
        if data[i][0] in list_A or data[i][1] in list_A:
            if data[i][0] not in list_B and data[i][1] not in list_B:
                t = np.array(data[i]).reshape(1,3)
                res = np.append(res,t,0)
    res = np.delete(res,0,0)
    return res

def Make_dictionary(data , Set):
    if len(data) == 0:
        dict2 = {}
        for i in range(len(Set)):
            dict2[i+1] = Set[i]
            Set[i] = i+1
        return data,dict2,Set

    m = data.max()
    m = int(m)
    dict1 = {}
    dict2 = {}
    Cal = np.zeros(shape=(1,m+1))
    for i in range(len(data)):
        Cal[0][int(data[i][0])] = 1
        Cal[0][int(data[i][1])] = 1

    count = 1
    for i in range(m+1):
        if Cal[0][i] > 0:
            Cal[0][i] = count
            dict1[i] = count
            dict2[count] = i
            count = count + 1

    for i in range(len(data)):
        data[i][0] = dict1[data[i][0]]
        data[i][1] = dict1[data[i][1]]

    for i in range(len(Set)):
        Set[i] = dict1[Set[i]]

    return data,dict2,Set