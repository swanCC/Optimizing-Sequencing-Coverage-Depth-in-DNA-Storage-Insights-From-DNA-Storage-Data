import numpy as np

mu_lognorm = 6.347523782081259  # 对数变换后的正态分布均值
sigma_lognorm = np.sqrt(0.964425042840954)  # 对数变换后的正态分布标准差
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

    # 初始化已经抽到的不同序列的集合
    drawn_sequences = set()
    total_draws = 0

    # 模拟有放回的加权抽样
    while len(drawn_sequences) < 0.5*num_sequences:
        # 根据权重进行加权抽样
        drawn_sequence = np.random.choice(sample_size, p=weights)
        drawn_sequences.add(drawn_sequence)
        total_draws += 1  # 抽取的条数由序列的条数决定
    return total_draws

sample_size = len(positive_numbers)  # 样本池大小（有100000种不同的序列）
num_sequences = len(positive_numbers)  # 每种序列至少抽到一次

draw_list = []
# 运行优惠券收集问题模拟
for i in range(500):
    total_draws = coupon_collector_with_weighted_sampling(sample_size, num_sequences)
    print(f"第{i + 1}次模拟：总共抽取了 {total_draws} 次，直到50%的序列都至少抽到一次。")
    draw_list.append(total_draws)
print('P30 500次模拟结果为', draw_list)
print('均值为：',np.mean(draw_list),'最大值：',max(draw_list),'最小值：',min(draw_list))