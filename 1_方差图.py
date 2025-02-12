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
f_prime = f

# 将符号表达式转换为可调用的函数
f_prime_func = lambdify((K, p, m), f_prime, 'numpy')

# 定义p的值
p_values = [0.000087, 0.000084, 0.0000706]

# 定义m的值列表
m_values = [11520, 11520, 11520]  # 示例：假设每个p对应相同的m值

# 创建图形
plt.figure(figsize=(8, 6))

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
    plt.plot(K_over_m_values, f_prime_values, label=lll[i], color=colors[i], linestyle=linestyle)

# 设置纵坐标范围从-0.00001开始
plt.ylim(bottom=-0.00001)

# 设置横坐标刻度为1为间隔
plt.xticks(np.arange(0, 11, 1))

# 设置标题和坐标轴标签
plt.xlabel('Coverage depth', fontsize=22)  # 增大坐标轴标签字号
plt.ylabel("f(K)", fontsize=22)  # 增大坐标轴标签字号

# 增大刻度标签字号
plt.tick_params(axis='both', which='major', labelsize=20)

# 显示图例
plt.legend(loc='upper right', fontsize=20)  # 增大图例字号

# 显示图形
plt.tight_layout()
plt.savefig('方差函数.png')
plt.show()
