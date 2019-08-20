def swap(data_A, dict_A, Set_A, data_B, dict_B, Set_B):
    size_A = len(Set_A)
    size_B = len(Set_B)
    if size_A > size_B:
        data_A,data_B = data_B,data_A
        dict_A,dict_B = dict_B,dict_A
        Set_A,Set_B = Set_B,Set_A

    return data_A, dict_A, Set_A, data_B, dict_B, Set_B

def Find_Origin_Set(data,dict,dict_F,dict_G):
    for i in range(len(data)):
        data[i] = dict[data[i]];
    if len(dict_F) > 0:
        for i in range(len(data)):
            data[i] = dict_F[data[i]];
    if len(dict_G) > 0:
        for i in range(len(data)):
            data[i] = dict_G[data[i]];
    return data

def Cal_similarity(data):
    index = 0;
    s = 0;
    n = len(data)
    for i in range(4):
        cnt = 0;
        for j in range(i*16+1,i*16+17):
            if j in data:
                cnt = cnt + 1;
        tmp_s = cnt/(n+16)
        if tmp_s > s:
            s = tmp_s
            index = i+1

    return index,s;


