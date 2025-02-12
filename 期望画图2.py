import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# 自定义列表数据，并计算倒数
uniform = [1/x for x in [0.394, 0.632, 0.777, 0.865, 0.918, 0.95, 0.970, 0.982, 0.989, 0.993, 0.996, 0.998, 0.998, 0.999, 0.999, 1, 1, 1, 1, 1]]
PCR10 = [1/x for x in [0.341, 0.521, 0.634, 0.712, 0.766, 0.807, 0.84, 0.863, 0.884, 0.9, 0.912, 0.924, 0.933, 0.94, 0.947, 0.953, 0.958, 0.962, 0.965, 0.968]]
PCR30 = [1/x for x in [0.317, 0.483, 0.592, 0.666, 0.72, 0.762, 0.795, 0.822, 0.843, 0.861, 0.877, 0.889, 0.9, 0.91, 0.918, 0.925, 0.931, 0.938, 0.943, 0.947]]
PCR60 = [1/x for x in [0.259, 0.399, 0.495, 0.565, 0.618, 0.661, 0.696, 0.725, 0.749, 0.771, 0.788, 0.805, 0.819, 0.832, 0.843, 0.852, 0.862, 0.87, 0.877, 0.885]]

# 创建x轴数据
x = np.linspace(0.5, 10, 20)  # 从0.5到10，共20个点

# 确保所有y数据长度一致
assert len(x) == len(uniform) == len(PCR10) == len(PCR30) == len(PCR60)

# 设置图形大小
plt.figure(figsize=(10, 6))

# 绘制折线图
plt.plot(x, PCR10, label='PCR10_cal_Thm1', color='#a3c0fb', marker='o', linestyle='--', markersize=4)  # 设置为虚线，标记大小为4
plt.plot(x, PCR30, label='PCR30_cal_Thm1', color='#d969af', marker='o', linestyle='--', markersize=4)
plt.plot(x, PCR60, label='PCR60_cal_Thm1', color='#fcd3df', marker='o', linestyle='--', markersize=4)  # 设置为虚线，标记大小为4
plt.plot(x, uniform, label='Uniform_cal_Thm2', color='#305299', marker='o', markersize=4)

# 添加标题和标签
plt.xlabel('Coverage depth', fontsize=18)
plt.ylabel('Coding redundancy', fontsize=18)

# 设置x轴和y轴的刻度
# 横坐标范围从0到10，每0.5为一刻度
plt.xticks(np.arange(0, 10.5, 0.5), fontsize=16, rotation=45)

# 设置y轴的刻度
plt.yticks([1, 1.5, 2, 2.5, 3, 3.5, 4], ['1', '1.5', '2', '2.5', '3', '3.5', '4'], fontsize=16)
ax = plt.gca()

# 确保最大值显示在坐标轴上
plt.xlim(0, 10)
plt.ylim(0.95, 4)  # 设置纵坐标的最小值为0.95，最大值为4

# 添加特殊标注
stars_x = [0.93, 1.08, 1.62]
stars_y = [2, 2, 2]
stars_colors = ['#67abd2', '#d7887f', '#f5b184']  # 红色、黄色、红紫色

# 绘制星星
plt.scatter(stars_x, stars_y, c=stars_colors, s=200, marker='*')

# 添加默认图例
default_legend = plt.legend(loc='upper left', bbox_to_anchor=(0, 1), ncol=1, fontsize=16)

# 创建自定义图例项
custom_lines = [
    Line2D([0], [0], color='w', marker='*', markersize=15, markerfacecolor='#67abd2', label='PCR10_sim_R=2'),
    Line2D([0], [0], color='w', marker='*', markersize=15, markerfacecolor='#d7887f', label='PCR30_sim_R=2'),
    Line2D([0], [0], color='w', marker='*', markersize=15, markerfacecolor='#f5b184', label='PCR60_sim_R=2')
]

# 合并图例项
all_handles = [*default_legend.legendHandles, *custom_lines]
all_labels = [text._text for text in default_legend.texts] + [line.get_label() for line in custom_lines]

# 添加自定义图例
plt.legend(all_handles, all_labels, loc='lower right', bbox_to_anchor=(1, 0.35), ncol=1, fontsize=16)

# 调整子图位置
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2, wspace=0.2, hspace=0.2)

# 显示图形
plt.savefig('期望图2.png')
plt.show()
