import csv

def count_occurrences_in_csv(file_path, search_term):
    count = 0
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # 遍历每一行，查找包含特定内容的行
        for row in reader:
            count += row.count(search_term)  # 统计当前行中出现的次数
    return count

# 示例使用
file_path = 'P10_best_hits.csv'  # 你的CSV文件路径
search_term = 'seq10467'      # 你要查找的特定内容
occurrences = count_occurrences_in_csv(file_path, search_term)
print(f"'{search_term}' 出现了 {occurrences} 次")


