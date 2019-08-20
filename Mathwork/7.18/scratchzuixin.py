def print_array(array):
    for i in range(0, 64):
        for j in range(0, 64):
            print(str(int(array[i][j])) + " ", end="");
        print("\n");

def generate_random_network_with_certain_ratio(array, per):
    r"""生成网络结构相同、给定正负边比例的随机网络

    :param array: 提供网络结构的矩阵，网络的正负边情况没有影响.
    :param per: 负边占全部边的比例.
    :return: 与输入网络结构相同、给定正负边比例的随机网络
    :rtype: numpy.array
    """
    temp = array.copy()
    [x, y] = np.where(np.triu(temp) != 0)
    num_of_edges = int(len(x))
    num_of_neg = int(num_of_edges * per)
    index_neg = np.random.choice(num_of_edges, num_of_neg,replace = False)
    index_pos = list(set(np.arange(num_of_edges)).difference(set(index_neg)))
    temp[x[index_neg], y[index_neg]] = -1
    temp[y[index_neg], x[index_neg]] = -1
    temp[x[index_pos], y[index_pos]] = 1
    temp[y[index_pos], x[index_pos]] = 1
    return temp


import networkx as nx
import numpy as np
import sys

for jj in range(1,10):
    for y in range(8,16,1):
        ii = 0;
        # for jj in range(2,10):
        while ii < 10:
            iii = ii + 1

            # 规模
            arrays = np.zeros((64, 64))
            random_conuter = np.zeros(64)
            # 定义
            num_intra = y;
            # 结构向内外连边数
            num_inter = 16 - y;
            # 负边比例
            neg = '0.' + str(jj)
            rate_neg = eval(neg)
            # rate_neg = 0.9


            flag = 1;
            # 输出
            cnt = 0
            while cnt < 4:
                G = nx.random_graphs.random_regular_graph(num_intra, 16)
                for i in range(0, 16):
                    for j in range(0, 16):
                        if (G.has_edge(i, j)):
                            arrays[cnt * 16 + i][cnt * 16 + j] = 1
                cnt = cnt + 1

            for i in range(62, -1, -2):
                cnt = 0;
                while random_conuter[i] < num_inter and flag == 1:
                    x = np.random.randint(0, 64);
                    cnt = cnt + 1;
                    if cnt > 10000:
                        flag = flag + 1;
                        break;
                    if int(i / 16) != int(x / 16) and random_conuter[x] < num_inter:
                        arrays[i][x] = 1;
                        arrays[x][i] = 1;
                        random_conuter[x] = random_conuter[x] + 1;
                        random_conuter[i] = random_conuter[i] + 1;

            for i in range(1, 64, 2):
                cnt = 0;
                while random_conuter[i] < num_inter and flag == 1:
                    x = np.random.randint(0, 64);
                    cnt = cnt + 1
                    if cnt > 10000:
                        flag = flag + 1;
                        break;
                    if int(i / 16) != int(x / 16) and random_conuter[x] < num_inter:
                        arrays[i][x] = 1;
                        arrays[x][i] = 1;
                        random_conuter[x] = random_conuter[x] + 1;
                        random_conuter[i] = random_conuter[i] + 1;

            if (flag > 1):
                continue
            print('done');
            arrays = generate_random_network_with_certain_ratio(arrays, rate_neg);
            ii = ii + 1;

            # -----------------------------------输出-----------------------------------------------

            filename = str(num_intra) + '-' + str(num_inter) + '-' + str(iii) + '-' + str(rate_neg)
            filename = 'D:/7.18/' + filename + '.txt'
            # 文件位置"""
            f = open(filename, 'w+')
            for i in range(0, 64):
                for j in range(0, 64):
                    if arrays[i][j] != 0:
                        f.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(int(arrays[i][j])) + '\n')
            f.close()

            # for i in range(0, 16):
            #     for j in range(0, 16):
            #         if arrays[i][j] != 0:
            #             f.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(int(arrays[i][j])) + '\n')
            # f.close()
            #
            # # print_array(arrays)
            # # print(random_conuter)
            # filename = str(num_intra) + '-' + str(num_inter) + '-' + str(iii) + '-' + '2' + '-' + str(rate_neg)
            # filename = 'D:/6.26/' + filename + '.txt'
            # # 文件位置"""
            # f = open(filename, 'w+')
            #
            # for i in range(16, 32):
            #     for j in range(16, 32):
            #         if arrays[i][j] != 0:
            #             f.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(int(arrays[i][j])) + '\n')
            # f.close()
            #
            # filename = str(num_intra) + '-' + str(num_inter) + '-' + str(iii) + '-' + '3' + '-' + str(rate_neg)
            # filename = 'D:/6.26/' + filename + '.txt'
            # # 文件位置"""
            # f = open(filename, 'w+')
            #
            # for i in range(32, 48):
            #     for j in range(32, 48):
            #         if arrays[i][j] != 0:
            #             f.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(int(arrays[i][j])) + '\n')
            # f.close()
            #
            # filename = str(num_intra) + '-' + str(num_inter) + '-' + str(iii) + '-' + '4' + '-' + str(rate_neg)
            # filename = 'D:/6.26/' + filename + '.txt'
            # # 文件位置"""
            # f = open(filename, 'w+')
            #
            # for i in range(48, 64):
            #     for j in range(48, 64):
            #         if arrays[i][j] != 0:
            #             f.write(str(i + 1) + ' ' + str(j + 1) + ' ' + str(int(arrays[i][j])) + '\n')
            # f.close()
            # -----------------------------------输出-----------------------------------------------

    #print(over);
    print(y,jj);