import math
import numpy as np
K = [2500,5000,7500,10000,12500,15000]
m = 5000

# 用3σ原则去离群值，保存在result列表里
def filter_and_sort_numbers(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 解析出所有的数字
    import re
    numbers = [int(num) for num in re.findall(r'\b\d+\b', content)]

    # 过滤掉大于1024和小于20的数字
    #filtered_numbers = [num for num in numbers if num > 0]

    # 排序
    sorted_numbers = sorted(numbers)

    return sorted_numbers

# 调用函数并打印结果
file_path = 'P30不带seq.txt'  # 替换为你的文件路径
result = filter_and_sort_numbers(file_path)
print(np.mean(result))
n = 0
for item in result:
    n+=item
print(n)




'''for ele in K:
    print('--------------------抽取', ele, '条序列的情况--------------------')
    E_lst = []
    Var_lst = []
    for i in range(1,11):
        positive_random_numbers = []
        n = 0
        E = 0
        Var1 = 0
        Var2 = 0
        Var3 = 0

        # 将正数部分添加到列表中
        sampled_data = np.random.choice(result, size=m, replace=True)
        positive_random_numbers = sampled_data

        for item in positive_random_numbers[0:m]:
            n+=item
        #print('n=',n)

        for j in range(0,m):
            E+=1-math.exp(-ele*positive_random_numbers[j]/n)
            Var1+=(1-math.exp(-ele*positive_random_numbers[j]/n))*(math.exp(-ele*positive_random_numbers[j]/n))
            Var2+=(positive_random_numbers[j]/n) * (math.exp(-ele*positive_random_numbers[j]/n))
        Var3 = Var1 - ele*((Var2)**2)
        E_lst.append(E)
        Var_lst.append(Var3)
        #print('E(S)=',E)
        #print('Var(S)=',Var3)
    print('E_lst:',E_lst)
    print('Var_lst:',Var_lst)
    print('抽取',ele,'条序列的E(S)的均值为：',np.mean(E_lst))
    print('抽取',ele,'条序列的Var(S)的均值为：',np.mean(Var_lst))'''
