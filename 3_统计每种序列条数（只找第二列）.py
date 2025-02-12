import pandas as pd
import re

# Step 1: 读取CSV文件的第二列并统计每个目标内容出现的次数
def count_occurrences(file_path, start, end, output_file):
    term_counts = {f"seq{num}": 0 for num in range(start, end+1)}  # 初始化字典，用于存储每个seqX的计数
    df = pd.read_csv(file_path, usecols=[1])  # 读取CSV文件的第二列（索引从0开始，第二列是索引1）

    # 查找seqX的内容
    for num in range(start, end+1):
        search_term = f"seq{num}"
        # 使用精确匹配查找目标内容 "seqX"
        pattern = f"^{re.escape(search_term)}$"  # 精确匹配 "seqX"，不允许后面有其他字符
        # 仅对第二列进行查找
        term_counts[search_term] += df.iloc[:, 0].astype(str).str.contains(pattern).sum()

    # Step 2: 将统计结果保存到txt文件
    with open(output_file, 'w') as f:
        for term, count in term_counts.items():
            f.write(f"{term}: {count}\n")

    print(f"结果已保存到 {output_file}")

# 示例使用
file_path = 'P60_best_hits.csv'  # CSV文件路径

output_file = 'P60_seqkindsnum.txt'  # 输出的txt文件路径
start, end = 1, 11520  # 查找从 seq1 到 seq10000 的内容

# 获取每个目标内容的出现次数并保存到txt文件
count_occurrences(file_path, start, end, output_file)
