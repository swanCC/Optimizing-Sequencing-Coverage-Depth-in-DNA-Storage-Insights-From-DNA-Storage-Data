import numpy as np
import random
from numpy.linalg import cholesky
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

sampleNo = 500000 #共多少种序列
select_num =3000000 #测序时抽样多少条

mu_list = []
var_list = []

for j in range(5):
    result_list = []  # 抽取select_num条中不同种类数的集合
    my_list = []
    value = 100  # 每种序列条数
    for i in range(sampleNo):
        my_list.append(value)

    for k in range(20):
        ran_test = []
        order = 0
        for element in my_list:
            s = [element] #s=[100,100,...,100]共sampleNo个100，此步是为转成序列
            # s = s.astype(int) #浮点型转换为整型
            order = order + 1
            for seq_num in s:  # 遍历随机数序列中的每个元素seq_num
                for p in range(0, seq_num):
                    ran_test.append(order)  # 构建测试序列
        temp_test = ran_test
        # s={10,10,10}
        # seq_num=10, order=1, ran_test={1,...,1(9个)}
        # seq_num=10, order=2, ran_test={1,...,1(9个), 2,...,2(9个)}
        # seq_num=10, order=3, ran_test={1,...,1(9个), 2,...,2(9个), 3,...,3(9个)}
        # 最后temp_test就是测序准备池

        #select_out = np.random.shuffle(temp_test)  # 对temp_test随机洗牌，模拟随机抽样

        select_out = np.random.choice(temp_test, select_num, replace=True)  # 有放回抽样集合
        #print("抽样结果为：", select_out)
        out_num = len(set(select_out))  # 不同种类数
        result_list.append(out_num)
        print(out_num / sampleNo)  # 不同种类数/总种类数=抽取到的不同种序列的比例
        print("=" * 20)
    #print("抽取select_num条中不同种类序列数", result_list)  # 抽取select_num条中不同种类序列


    # 计算均值
    def mean(data):
        return sum(data) / len(data)


    # 计算方差
    mu = sampleNo * (1 - (((sampleNo - 1) / sampleNo) ** select_num))


    def variance(data):
        n = len(data)
        return sum((x - mu) ** 2 for x in data) / n


    data = result_list
    mu_list.append(mean(result_list))
    var_list.append(variance(result_list))
    #print(mean(result_list), variance(result_list))
print("mu_list为：", mu_list)
print("var_list为：", var_list)
print('期望为：',np.mean(mu_list),'方差为：', np.mean(var_list))
'''sns.kdeplot(result_list)
plt.show()'''
