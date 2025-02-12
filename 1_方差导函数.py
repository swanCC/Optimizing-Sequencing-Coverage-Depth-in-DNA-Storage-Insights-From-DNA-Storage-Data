import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, exp, diff, lambdify
from matplotlib.patches import Ellipse
from scipy.optimize import fsolve
import matplotlib.patheffects as PathEffects

# 定义符号变量
K, p, m = symbols('K p m')

# 定义函数
f = exp(-p * K) - exp(-2 * p * K) - (m / K) * (p * K) ** 2 * exp(-2 * p * K)

# 对K求导
f_prime = diff(f, K)

# 将符号表达式转换为可调用的函数
f_prime_func = lambdify((K, p, m), f_prime, 'numpy')

# 定义p的值
p_values = [0.000087, 0.000084, 0.0000706]

# 定义m的值列表
m_values = [11520, 11520, 11520]  # 示例：假设每个p对应相同的m值

# 创建图形
plt.figure(figsize=(10, 6))

# 颜色列表，用于区分不同的p值
colors = ['#263C84', '#D969AF', '#EE7D31']
lll = ['PCR10', 'PCR30', 'PCR60']

# 循环遍历不同的p值和对应的m值
for i, (p_val, m_val) in enumerate(zip(p_values, m_values)):
    # 生成K的值，使得K/m覆盖从1到10的范围
    K_values = np.linspace(0, 10 * m_val, 400)

    # 计算导函数的值
    f_prime_values = f_prime_func(K_values, p_val, m_val)

    # 计算K/m的值
    K_over_m_values = K_values / m_val

    # 确定线条样式
    linestyle = '-' if colors[i] == '#263C84' else '-'

    # 绘制导函数的图像
    plt.plot(K_over_m_values, f_prime_values, label=lll[i], color=colors[i], linestyle=linestyle, linewidth=2)

# 添加f'(K)=0的渐近线，用红色虚线表示
plt.axhline(y=0, color='red', linestyle='--', label='f\'(K)=0', linewidth=1.5)

# 设置纵坐标范围从-0.00001开始
plt.ylim(bottom=-0.00001)

# 设置横坐标刻度为1为间隔
plt.xticks(np.arange(0, 11, 1), fontsize=16)

# 设置纵坐标刻度为1为间隔，并设置字号为16
plt.yticks(fontsize=16)

# 设置标题和坐标轴标签
plt.xlabel('Coverage depth', fontsize=18)
plt.ylabel("f'(K)", fontsize=18)

# 在(1.3, 0)处绘制一个长0.5宽1的空心椭圆
ellipse = Ellipse(xy=(1.3, 0), width=0.5, height=0.000001,
                  edgecolor='red', facecolor='none', linestyle='-', linewidth=2)
ax = plt.gca()
ax.add_patch(ellipse)

# 在椭圆右上角画一个黑色箭头并标注“Maximum Variance Points”
arrow_x = 1.3 + 0.5 / 2  # 椭圆中心x坐标加上宽度的一半
arrow_y = 0.000001       # 箭头稍微高于椭圆
plt.annotate(
    "Maximum \n Variance \n Points",
    xy=(arrow_x, arrow_y),
    xytext=(arrow_x + 0.02, arrow_y + 0.0000015),  # 增加y坐标的值以增大倾角
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=2, shrinkA=5, shrinkB=1),
    fontsize=16,
    ha='left',
    va='bottom'
)

# 画从(7, 0)到(7, -0.00001)的红色虚线
plt.plot([1.25, 1.25], [0, -0.00001], color='red', linestyle='--', linewidth=1.5)

# 画从(8, 0)到(8, -0.00001)的红色虚线
plt.plot([1.33, 1.33], [0, -0.00001], color='red', linestyle='--', linewidth=1.5)
plt.plot([7, 7], [0, -0.00001], color='red', linestyle='--', linewidth=1.5)
plt.plot([8, 8], [0, -0.00001], color='red', linestyle='--', linewidth=1.5)

# 显示图例，并手动设置位置
plt.legend(loc=(0.8, 0.01), fontsize=16)  # 你可以根据需要调整 (0.7, 0.7) 的值来改变图例的位置

# 显示图形
plt.tight_layout()
#plt.savefig('方差导函数.png')
plt.show()
