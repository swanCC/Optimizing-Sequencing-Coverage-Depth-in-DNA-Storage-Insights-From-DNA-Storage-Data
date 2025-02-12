import numpy as np

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
file_path = 'P60不带seq.txt'  # 替换为你的文件路径
result = filter_and_sort_numbers(file_path)
print('数据为：',result)
print(len(result))

# 计算加和
P10_sum = sum(result)
print('序列总条数：', P10_sum)

# 用每个数字除以加和
P10_normalized = [number / P10_sum for number in result]

def coupon_collector_with_weighted_sampling(sample_size, num_sequences):
    weights = P10_normalized  # 每个序列的抽样权重

    # 初始化已经抽到的不同序列的计数
    drawn_sequences_count = [0] * sample_size
    total_draws = 0

    # 模拟有放回的加权抽样
    while sum(count >= 2 for count in drawn_sequences_count) < 0.8 * num_sequences: #a=2,R=1.25
        # 根据权重进行加权抽样
        drawn_sequence = np.random.choice(sample_size, p=weights)
        drawn_sequences_count[drawn_sequence] += 1
        total_draws += 1  # 抽取的条数由序列的条数决定

    return total_draws

# 设置参数
sample_size = len(P10_normalized)  # 样本池大小（有100000种不同的序列）
num_sequences = len(P10_normalized)  # 每种序列至少抽到两次

draw_list = []
# 运行优惠券收集问题模拟
for i in range(400):
    total_draws = coupon_collector_with_weighted_sampling(sample_size, num_sequences)
    print(f"第{i + 1}次模拟：总共抽取了 {total_draws} 次，直到80%的序列都至少抽到两次。")
    draw_list.append(total_draws)
print('P60 400次模拟结果为', draw_list)
draw_avg = np.mean(draw_list)
draw_min = min(draw_list)
draw_max = max(draw_list)
print('平均抽取了', draw_avg, '次', '最大值：', draw_max, '最小值：', draw_min)