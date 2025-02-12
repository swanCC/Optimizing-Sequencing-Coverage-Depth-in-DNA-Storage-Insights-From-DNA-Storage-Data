# Optimizing-Sequencing-Coverage-Depth-in-DNA-Storage-Insights-From-DNA-Storage-Data
1.先用blastn处理原始fastq数据并以outfmt6格式输出，生成P10_results.txt、P30_results.txt、P60_results.txt三个文件
2.调用“1_找最大相似同源序列.py”生成Pxx_best_hits.csv
3.调用“2_统计每种序列条数.py”生成Pxx_seqkindnum.txt，其中内容格式为seqxx:xxx（原始oligopool中的第几种序列被扩增了多少条）
4.提取Pxx_seqkindnum.txt中第二列条数信息，保存为“Pxx不带seq.txt”
5.分别运行“3_P10/30/60数据统计.py”，生成“PCR10/30/60_data.png”
