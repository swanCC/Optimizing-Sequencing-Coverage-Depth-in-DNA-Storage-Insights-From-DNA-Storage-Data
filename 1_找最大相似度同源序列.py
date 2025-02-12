import pandas as pd

def process_blast_output(blast_file):
    # 读取BLAST outfmt6输出文件
    # 假设BLAST的输出是制表符分隔的，并且列顺序是 qseqid, sseqid, pident, length, mismatch, gapopen, qstart, qend, sstart, send, evalue, bitscore
    df = pd.read_csv(blast_file, sep='\t', header=None,
                     names=['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen',
                            'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'])

    # 按照 qseqid 分组
    grouped = df.groupby('qseqid')

    result = []

    # 对每个查询序列进行处理
    for qseqid, group in grouped:
        # 在组内找到具有最高相似度的目标序列
        # 通常可以使用 pident（百分比相似度）来找到最高相似度的序列
        best_hit = group.loc[group['pident'].idxmax()]

        # 提取最佳匹配的查询序列ID和目标序列ID
        best_qseqid = best_hit['qseqid']
        best_sseqid = best_hit['sseqid']
        best_pident = best_hit['pident']
        best_bitscore = best_hit['bitscore']

        # 将结果保存到列表中
        result.append({
            'qseqid': best_qseqid,
            'sseqid': best_sseqid,
            'pident': best_pident,
            'bitscore': best_bitscore
        })

    # 将结果转换为DataFrame并返回
    result_df = pd.DataFrame(result)
    return result_df

# 调用函数并输出结果
blast_file = 'P60_results.txt'  # 替换为你的BLAST输出文件路径
result_df = process_blast_output(blast_file)

# 打印结果
print(result_df)

# 可选择将结果保存到新的文件
result_df.to_csv('P60_best_hits.csv', index=False)
