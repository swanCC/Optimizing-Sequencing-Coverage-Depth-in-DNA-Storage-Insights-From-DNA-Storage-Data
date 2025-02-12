import numpy as np

mu_lognorm = 5.9787337041228765  # 对数变换后的正态分布均值
sigma_lognorm = np.sqrt(1.3782151166957604)  # 对数变换后的正态分布标准差
result_list = []
# 生成对数正态分布数据
s = np.random.lognormal(mean=mu_lognorm, sigma=sigma_lognorm, size=11520)
# 过滤掉小于等于0的值（理论上对数正态分布不会出现负数，但数值计算可能会有极小概率出现）
positive_numbers = s[s > 0] #positive_numbers代表总体

PCR_sum = sum(positive_numbers)
print('序列总条数：', PCR_sum)

# 用每个数字除以加和
PCR_normalized = [number / PCR_sum for number in positive_numbers]

def coupon_collector_with_weighted_sampling(sample_size, num_sequences):
    weights = PCR_normalized  # 每个序列的抽样权重

    # 初始化已经抽到的不同序列的计数
    drawn_sequences_count = [0] * sample_size
    total_draws = 0

    # 模拟有放回的加权抽样
    while sum(count >= 2 for count in drawn_sequences_count) < 0.8 * num_sequences:
        # 根据权重进行加权抽样
        drawn_sequence = np.random.choice(sample_size, p=weights)
        drawn_sequences_count[drawn_sequence] += 1
        total_draws += 1  # 抽取的条数由序列的条数决定

    return total_draws

# 设置参数
sample_size = len(PCR_normalized)  # 样本池大小（有100000种不同的序列）
num_sequences = len(PCR_normalized)  # 每种序列至少抽到两次

draw_list = []
# 运行优惠券收集问题模拟
for i in range(500):
    total_draws = coupon_collector_with_weighted_sampling(sample_size, num_sequences)
    print(f"第{i + 1}次模拟：总共抽取了 {total_draws} 次，直到80%的序列都至少抽到两次。")
    draw_list.append(total_draws)
print('P60 500次模拟结果为', draw_list)
draw_avg = np.mean(draw_list)
draw_min = min(draw_list)
draw_max = max(draw_list)
print('平均抽取了', draw_avg, '次', '最大值：', draw_max, '最小值：', draw_min)