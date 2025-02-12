import matplotlib.pyplot as plt
from collections import Counter

# 用3σ原则去离群值，保存在result列表里
def filter_and_sort_numbers(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 解析出所有的数字
    import re
    numbers = [int(num) for num in re.findall(r'\b\d+\b', content)]

    # 排序
    sorted_numbers = sorted(numbers)

    return sorted_numbers

# 调用函数并打印结果
file_path = 'P30不带seq.txt'  # 替换为你的文件路径
result = filter_and_sort_numbers(file_path)
print(result)

# 使用Counter来统计每个数字的出现频率
frequency = Counter(result)

# 准备绘图数据
numbers = list(frequency.keys())
counts = list(frequency.values())

# 创建一个颜色列表，用于区分只出现一次的数字
#linewidths = [0 if count > 1 else 0.5 for count in counts]  # 只出现一次的数字加粗边框

# 设置图形大小为 (8, 6)
plt.figure(figsize=(6, 6))

# 绘制直方图
plt.bar(numbers, counts, color='#D969AF', edgecolor='#D969AF', linewidth=0.2)
plt.xlabel('Copy numbers', fontsize=20)  # 设置横坐标标签的字号
plt.ylabel('Frequency', fontsize=20)  # 设置纵坐标标签的字号

# 设置纵坐标范围
plt.ylim(0, 30)

# 增加坐标刻度的字号
plt.xticks(fontsize=18, rotation=30)  # 横坐标刻度的字号
plt.yticks(fontsize=18)  # 纵坐标刻度的字号和旋转角度

# 调整子图的位置和大小，使其占满画布
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.19, top=0.9)

'''# 获取当前的 Axes 对象并设置坐标轴线宽
ax = plt.gca()
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)'''

# 保存为 PDF 格式
plt.savefig('PCR30_data.png', format='png')  # 保存为 PDF 格式
plt.show()
