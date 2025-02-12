import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# 横坐标范围从0到13，每1为一刻度
x_min, x_max = 0, 13
x_ticks = np.arange(0, 13.5, 1)  # 每1为一刻度

# 纵坐标范围从0到1
y_min, y_max = 0, 1

# 数据
PCR10 = [2.35, 1.42, 5.12]
PCR30 = [2.77, 1.85, 6.65]
PCR60 = [4.24, 3.33, 12]

# 颜色配置
colors_PCR10 = ['#263c84', '#263c84', '#263c84']
colors_PCR30 = ['#d969af', '#d969af', '#d969af']
colors_PCR60 = ['#f5b184', '#f5b184', '#f5b184']

# 标记
labels_PCR10 = ['exp_max', 'lower theoretical bound of Thm 3', 'lower theoretical bound of Thm 4']
labels_PCR30 = ['exp_max', 'lower theoretical bound of Thm 3', 'lower theoretical bound of Thm 4']
labels_PCR60 = ['exp_max', 'lower theoretical bound of Thm 3', 'lower theoretical bound of Thm 4']

# 创建图形
plt.figure(figsize=(12, 6))

# 绘制坐标轴
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(x_ticks, fontsize=12)
plt.yticks([])  # 隐藏纵坐标刻度

# 绘制 PCR10 数据
handles_PCR10 = []
for i, (x, color, label) in enumerate(zip(PCR10, colors_PCR10, labels_PCR10)):
    if label == 'exp_max':
        line = plt.axvline(x=x, color=color, linestyle='-', linewidth=2, label=label)  # 实线
    elif label == 'lower theoretical bound of Thm 3':
        line = plt.axvline(x=x, color=color, linestyle='dotted', linewidth=3, label='lower theoretical bound of Thm 3')  # 虚线
    else:
        line = plt.axvline(x=x, color=color, linestyle='--', linewidth=2, label='lower theoretical bound of Thm 4')  # 点虚线
    handles_PCR10.append(line)

# 绘制 PCR30 数据
handles_PCR30 = []
for i, (x, color, label) in enumerate(zip(PCR30, colors_PCR30, labels_PCR30)):
    if label == 'exp_max':
        line = plt.axvline(x=x, color=color, linestyle='-', linewidth=2, label=label)  # 实线
    elif label == 'lower theoretical bound of Thm 3':
        line = plt.axvline(x=x, color=color, linestyle='dotted', linewidth=3, label='lower theoretical bound of Thm 3')  # 虚线
    else:
        line = plt.axvline(x=x, color=color, linestyle='--', linewidth=2, label='lower theoretical bound of Thm 4')  # 点虚线
    handles_PCR30.append(line)

# 绘制 PCR60 数据
handles_PCR60 = []
for i, (x, color, label) in enumerate(zip(PCR60, colors_PCR60, labels_PCR60)):
    if label == 'exp_max':
        line = plt.axvline(x=x, color=color, linestyle='-', linewidth=2, label=label)  # 实线
    elif label == 'lower theoretical bound of Thm 3':
        line = plt.axvline(x=x, color=color, linestyle='dotted', linewidth=3, label='lower theoretical bound of Thm 3')  # 虚线
    else:
        line = plt.axvline(x=x, color=color, linestyle='--', linewidth=2, label='lower theoretical bound of Thm 4')  # 点虚线
    handles_PCR60.append(line)

# 添加标题和标签
plt.xlabel('Coverage depth', fontsize=14)

# 手动创建图例
# 创建代理艺术家来表示图例标题
title_PCR10 = Line2D([0], [0], color='w', lw=0)
title_PCR30 = Line2D([0], [0], color='w', lw=0)
title_PCR60 = Line2D([0], [0], color='w', lw=0)

# 创建图例
first_group = [title_PCR10] + handles_PCR10
second_group = [title_PCR30] + handles_PCR30
third_group = [title_PCR60] + handles_PCR60

# 合并所有图例项
all_handles = first_group + second_group + third_group
all_labels = ['PCR10'] + ['exp_max', 'lower theoretical bound of Thm 3', 'lower theoretical bound of Thm 4'] + \
             ['PCR30'] + ['exp_max', 'lower theoretical bound of Thm 3', 'lower theoretical bound of Thm 4'] + \
             ['PCR60'] + ['exp_max', 'lower theoretical bound of Thm 3', 'lower theoretical bound of Thm 4']

# 显示图例
plt.legend(all_handles, all_labels, loc='center', bbox_to_anchor=(0.72, 0.35), bbox_transform=plt.gca().transAxes, fontsize=14)

# 显示图形
plt.tight_layout()
plt.savefig('a=2 R=2(2).pdf', format='pdf')
plt.show()
