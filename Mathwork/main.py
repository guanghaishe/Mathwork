from P7_community_detection import community_detection
from Fractions import *
import csv
import numpy as np

def takeSecond(elem):
    return elem[1]

if __name__ == '__main__':
    filepath = 'D:/python workspace/Mathwork/7.18/8-8-1-0.6'
    with open('D:/7.18/all.txt', 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for ii in range(8,16,8):
            for jj in range(1,11):
                for k in np.arange(0.1, 1, .1) :
                    filename = str(ii) + '-' + str(16-ii) + '-'+ str(jj) + '-'+ str(round(k,1))+ '.txt'
                    filename = filepath + filename
                    data = np.loadtxt('D:/python workspace/Mathwork/7.18/8-8-1-0.3.txt')
                    data_A, dict_A, Set_A, data_B, dict_B, Set_B = community_detection(data, 7)
                    '''
                    ********************
                    *******待改进*******
                    ********************
                    '''
                    if abs(len(Set_A) - len(Set_B)) <= 8:
                        data_C, dict_C, Set_C, data_D, dict_D, Set_D = community_detection(data_A, 8)
                        data_E, dict_E, Set_E, data_F, dict_F, Set_F = community_detection(data_B, 8)
                        Community_A = Find_Origin_Set(Set_C, dict_C, dict_A, [])
                        Community_B = Find_Origin_Set(Set_D, dict_D, dict_A, [])
                        Community_C = Find_Origin_Set(Set_E, dict_E, dict_B, [])
                        Community_D = Find_Origin_Set(Set_F, dict_F ,dict_B, [])

                    else:#abs(len(Set_A) - len(Set_B)) > 8:
                        data_A, dict_A, Set_A, data_B, dict_B, Set_B = swap(data_A, dict_A, Set_A, data_B, dict_B, Set_B)
                        Sets = [];dicts = [];
                        Set_A = Find_Origin_Set(Set_A,dict_A,[],[])
                        Sets.append(Set_A);dicts.append(dict_B);

                        data_C, dict_C, Set_C, data_D, dict_D, Set_D = community_detection(data_B, 8)
                        data_C, dict_C, Set_C, data_D, dict_D, Set_D = swap(data_C, dict_C, Set_C, data_D, dict_D, Set_D)
                        Set_C = Find_Origin_Set(Set_C,dict_C,dicts[0],[])
                        Sets.append(Set_C);dicts.append(dict_D);

                        data_E, dict_E, Set_E, data_F, dict_F, Set_F = community_detection(data_D, 8)
                        data_E, dict_E, Set_E, data_F, dict_F, Set_F = swap(data_E, dict_E, Set_E, data_F, dict_F, Set_F)
                        Set_E = Find_Origin_Set(Set_E, dict_E, dicts[1], dicts[0])
                        Set_F = Find_Origin_Set(Set_F, dict_F, dicts[1], dicts[0])
                        Sets.append(Set_E);
                        Sets.append(Set_F);


                        Community_A = Sets[0];
                        Community_B = Sets[1];
                        Community_C = Sets[2];
                        Community_D = Sets[3];

                    '''
                   ********************
                   *******统计*******
                   ********************
                   '''

                    num_to_Community = {1:Community_A, 2:Community_B, 3:Community_C, 4:Community_D}
                    res = []
                    for i in range(1,5):
                        index,s = Cal_similarity(num_to_Community[i])
                        res.append([i,index,s])
                    res.sort(key=takeSecond)

                    sum = 0
                    for i in range(len(res)):
                        sum = sum + res[i][2]

                    '''
                   ***********************
                   *******输出到文件*******
                   ***********************
                  '''
                    file_index = str(ii) + '-' + str(16 - ii) + '-' + str(jj) + '-' + str(round(k, 1))
                    writer.writerow([file_index , sum])







