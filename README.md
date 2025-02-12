# Optimizing-Sequencing-Coverage-Depth-in-DNA-Storage-Insights-From-DNA-Storage-Data
1.先用blastn处理原始fastq数据并以outfmt6格式输出，生成P10_results.txt、P30_results.txt、P60_results.txt三个文件
2.调用“1_找最大相似同源序列.py”生成Pxx_best_hits.csv
3.调用“2_统计每种序列条数.py”生成Pxx_seqkindnum.txt，其中内容格式为seqxx:xxx（原始oligopool中的第几种序列被扩增了多少条）
4.提取Pxx_seqkindnum.txt中第二列条数信息，保存为“Pxx不带seq.txt”
5.分别运行“3_P10/30/60数据统计.py”，生成“PCR10/30/60_data.png”
6.运行“4_对数正态拟合.py”，生成"log_PCR10/30/60.pdf"，由拟合直接得到样本分布参数，再由公式计算出总体分布参数
7.模型计算：①对数正态：“5_样本/总体对数正态模型计算.py”；②均匀分布：“5_均匀分布计算”，结果保存在“验证测序模型准确性.xlsx”的“对数正态”中
  蒙特卡洛（直接）模拟：①对数正态：“5_样本/总体对数正态蒙特卡洛模拟”；②均匀分布：“5_均匀分布模拟”，结果保存在“蒙特卡洛模拟.xlsx”中
