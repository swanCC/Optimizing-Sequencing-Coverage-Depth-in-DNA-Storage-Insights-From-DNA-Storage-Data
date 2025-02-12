#file:C:\Users\CRY\PycharmProjects\pythonProject1\1_对数正态.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import curve_fit
import re
from matplotlib import colors
from matplotlib.patches import Patch

def filter_and_sort_numbers(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 解析出所有的数字
    numbers = [int(num) for num in re.findall(r'\b\d+\b', content)]

    # 排序
    sorted_numbers = sorted(numbers)

    return sorted_numbers

# 定义正态分布的概率密度函数
def log_norm_pdf(x, mu, sigma):
    return norm.pdf(x, loc=mu, scale=sigma)

# 定义渐变颜色
cmap1 = colors.LinearSegmentedColormap.from_list("cmap1",
                                                 [(218 / 255, 227 / 255, 242 / 255), (38 / 255, 60 / 255, 132 / 255)])
cmap2 = colors.LinearSegmentedColormap.from_list("cmap2",
                                                 [(255 / 255, 242 / 255, 245 / 255), (217 / 255, 105 / 255, 175 / 255)])
cmap3 = colors.LinearSegmentedColormap.from_list("cmap3",
                                                 [(252 / 255, 229 / 255, 214 / 255), (238 / 255, 125 / 255, 49 / 255)])

# 调用函数并打印结果
file_path = 'P10不带seq.txt'  # 替换为你的文件路径
PCR10_result = filter_and_sort_numbers(file_path)
sum_10 = sum(PCR10_result)
norm_10 = [i / sum_10 for i in PCR10_result if i != 0]

file_path = 'P30不带seq.txt'  # 替换为你的文件路径
PCR30_result = filter_and_sort_numbers(file_path)
sum_30 = sum(PCR30_result)
norm_30 = [i / sum_30 for i in PCR30_result if i != 0]

file_path = 'P60不带seq.txt'  # 替换为你的文件路径
PCR60_result = filter_and_sort_numbers(file_path)
sum_60 = sum(PCR60_result)
norm_60 = [i / sum_60 for i in PCR60_result if i != 0]

# 假设这是你的三个归一化和对数变换后的数据列表
log_data1 = np.log(norm_10)  # 加上一个小的正值以避免对数变换时出现负数
log_data2 = np.log(norm_30)
log_data3 = np.log(norm_60)

# 创建一个包含三个子图的图形，并共享横坐标
datasets = [(log_data1, cmap1, 'Dataset PCR10', 'log_PCR10.png'),
            (log_data2, cmap2, 'Dataset PCR30', 'log_PCR30.png'),
            (log_data3, cmap3, 'Dataset PCR60', 'log_PCR60.png')]

for log_data, cmap, dataset_label, file_name in datasets:
    # 创建一个单独的图形
    fig, ax = plt.subplots(figsize=(6, 6))

    # 计算直方图的 bin 边界和频数
    counts, bin_edges = np.histogram(log_data, bins=50, density=True)
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

    # 创建 CenteredNorm 对象，设置 vcenter 为 counts 的中间值
    vcenter = np.median(counts)
    norm_centered = colors.CenteredNorm(vcenter=vcenter)

    # 绘制直方图
    bar_container = ax.bar(bin_centers, counts, width=np.diff(bin_edges) * 0.9, color=cmap(norm_centered(counts)), edgecolor='black',
                           align='center',
                           alpha=1.0)  # 将透明度设置为1.0（不透明）

    # 计算数据值大于600的部分的均值和标准差
    log_data_greater_600 = [x for x in log_data if np.exp(x) > 0.000016]
    mean_log_greater_600 = np.mean(log_data_greater_600)
    std_log_greater_600 = np.std(log_data_greater_600)

    # 使用这些值作为初始参数
    initial_params = [mean_log_greater_600, std_log_greater_600]

    # 确保初始参数合理
    if len(initial_params) == 2 and not any(np.isnan(initial_params)):
        try:
            params, _ = curve_fit(log_norm_pdf, bin_centers, counts, p0=initial_params, maxfev=10000)
            x_fit = np.linspace(min(log_data), max(log_data), 1000)
            y_fit = norm.pdf(x_fit, loc=params[0], scale=params[1])
            fit_line, = ax.plot(x_fit, y_fit, 'red', label=f'norm dist.\nμ={params[0]:.2f}, σ={params[1]:.2f}')
        except Exception as e:
            print(f"Curve fitting failed: {e}")
    else:
        print("Initial parameters are invalid or NaN")

    # 计算整个数据集的均值
    mean_log_data = np.mean(log_data)

    # 在子图中绘制均值的红色虚线
    mean_line = ax.axvline(mean_log_data, color='red', linestyle='--', linewidth=2, label=f'Mean')

    # 添加图例
    handles = []
    labels = []

    # 添加拟合曲线的代理
    if 'fit_line' in locals():
        handles.append(fit_line)
        labels.append(fit_line.get_label())

    # 添加均值虚线的代理
    if 'mean_line' in locals():
        handles.append(mean_line)
        labels.append(mean_line.get_label())

    ax.legend(handles=handles, labels=labels, fontsize=12, loc='upper right')  # 强制图例显示在右上角

    # 设置图表标题和轴标签
    ax.set_ylabel('Density', fontsize=20)  # 增大纵坐标标签字号

    # 显示横坐标刻度数字
    ax.xaxis.set_tick_params(labelbottom=True, labelsize=18)  # 增大横坐标刻度字号

    # 设置纵坐标刻度
    ax.yaxis.set_ticks(np.arange(0, max(counts) + 0.05, 0.05))
    ax.yaxis.set_tick_params(labelsize=16)  # 增大纵坐标刻度字号

    # 设置横坐标标签
    ax.set_xlabel('Log. Proportion of different strands', fontsize=20)  # 增大横坐标标签字号

    # 调整子图之间的间距
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # 保存每个数据集的图像
    plt.savefig(file_name.replace('.png', '.pdf'), format='pdf')
    plt.close()  # 关闭当前图形，以便下一个图形可以被保存

    print(f"Saved {file_name.replace('.png', '.pdf')}")
