'''
Script for calculate the eigenvalues of an array.
mean    平均值
median  中位数
mode    众数
variance    方差
standard deviation  标准差
'''
import numpy as np
import argparse

parse = argparse.ArgumentParser(description='Calculate the eigenvalues of an array.')

parse.add_argument('--list', '-l', type=int, nargs='+', help='Input an array,values are sepatated by space.'
                                                             'Such as:1 2 34 5')

args = parse.parse_args()
data = args.list
# data = data.split(',')
# data = list(map(int, data))
data_mean = np.mean(data)
data_median = np.median(data)
# # bincount() 统计非负整数的个数，不能统计浮点数
counts = np.bincount(data)
data_mode = np.argmax(counts)
data_var = np.var(data)
data_std = np.std(data)
print(data)
# print(counts)
print(f"平均值：{data_mean}")
print(f"中位数：{data_median}")
print(f"众数：{data_mode}")
print(f"方差：{data_var}")
print(f"标准差：{data_std}")
