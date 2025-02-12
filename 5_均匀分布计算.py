import numpy as np

# 给定的参数
m = 10000
K_list = [3200,3300,3400]


# 计算均值和方差的函数
def compute_mean_and_variance(m, K):
    # 计算均值
    mean = m - m * np.exp(-K / m)

    # 计算方差
    variance = m * (1 - np.exp(-K / m)) * np.exp(-K / m) - K * np.exp(-2 * K / m)

    return mean, variance


# 遍历K值，计算对应的均值和方差
for K in K_list:
    mean, variance = compute_mean_and_variance(m, K)
    print(f"For K = {K}:")
    print(f"  Mean: {mean}")
    print(f"  Variance: {variance}")
    print()
