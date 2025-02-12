import numpy as np
import math
import matplotlib.pyplot as plt

# 使用 numpy 生成对数正态分布随机变量
m = 11520
K = [22*m,28*m,35*m]
for ele in K:
    print('--------------------抽取', ele, '条序列的情况--------------------')
    E_lst = []
    Var_lst = []
    for i in range(1,11):
        E = 0
        Var1 = 0
        Var2 = 0
        Var3 = 0

        # 对数正态分布参数
        mu_lognorm = -9.715701469301882  # 对数变换后的正态分布均值
        sigma_lognorm = np.sqrt(0.7378328624426234)  # 对数变换后的正态分布标准差
        result_list = []
        # 生成对数正态分布数据
        s = np.random.lognormal(mean=mu_lognorm, sigma=sigma_lognorm, size=m)
        # 过滤掉小于等于0的值（理论上对数正态分布不会出现负数，但数值计算可能会有极小概率出现）
        for item in s:
            if item < 0:
                print(item,'<0')
        positive_numbers = s[s > 0]
        sampled_data = positive_numbers
        #sampled_data = np.random.choice(positive_numbers, size=m, replace=False)

        for j in range(0,m):
            E += 1-math.exp(-ele*sampled_data[j])
            Var1 += (1-math.exp(-ele*sampled_data[j]))*(math.exp(-ele*sampled_data[j]))
            Var2 += sampled_data[j] * (math.exp(-ele*sampled_data[j]))
        Var3 = Var1 - ele*((Var2)**2)
        E_lst.append(E)
        Var_lst.append(Var3)
        '''print('E(S)=',E)
        print('Var(S)=',Var3)'''
    print('E_lst:',E_lst)
    print('Var_lst:',Var_lst)
    avg = np.mean(E_lst)
    avg_pro = avg/m
    print('抽取',ele,'条序列的E(S)的均值为：',avg_pro)
    #print('抽取',ele,'条序列的Var(S)的均值为：',np.mean(Var_lst))
