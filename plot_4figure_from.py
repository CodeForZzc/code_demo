"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/9/19 9:45
File : plot_4figure_from.py.py
Description :
从csv文件读取数据，同时画四个子图
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig = plt.figure(figsize=(10, 8))
plt.rcParams.update({"font.size": 15})

CSV_DIR = "./example_file/csv/qoe.csv"
all_data = pd.read_csv(CSV_DIR, sep=',')
data_array_qoe = np.array(all_data[['GCC_QoE', 'ARS-QoE', 'concerto_QoE', 'QoE']])

CSV_DIR = "./example_file/csv/rebuf.csv"
all_data = pd.read_csv(CSV_DIR, sep=',')
data_array_rebuf = np.array(all_data[['GCC_rebuf', 'ARS_rebuf', 'Concerto_rebuf', 'rebuf']])

CSV_DIR = "./example_file/csv/rtt.csv"
all_data = pd.read_csv(CSV_DIR, sep=',')
data_array_rtt = np.array(all_data[['GCC_rtt', 'ARS_rtt', 'Concerto_rtt', 'rtt']])

CSV_DIR = "./example_file/csv/send.csv"
all_data = pd.read_csv(CSV_DIR, sep=',')
data_array_send = np.array(all_data[['GCC_bitrate', 'ARS_bitrate', 'Concerto_bitrate', 'bitrate']])

plt.subplot(2, 2, 1)
cdf_gcc = data_array_qoe[:, 0]
cdf_ars = data_array_qoe[:, 1]
cdf_con = data_array_qoe[:, 2]
cdf_new = data_array_qoe[:, 3]
list = np.array(range(len(cdf_gcc)))
list = list / len(list)
plt.plot(cdf_gcc, list, linestyle=':', label="GCC", linewidth=2)
plt.plot(cdf_ars, list, linestyle='--', label="ARS", linewidth=2)
plt.plot(cdf_con, list, linestyle='-.', label="Concerto", linewidth=2)
plt.plot(cdf_new, list, linestyle='-', label="本发明", linewidth=2)
# plt.xlim(-10, 5)
# plt.ylim(0.0, 1.0)
plt.xlabel("平均用户体验质量QoE")
plt.ylabel("累计概率")
plt.title("QoE CDF曲线图")
max = np.max(data_array_qoe)
min = np.min(data_array_qoe)
print(max)
temp = min+(max-min)/2
plt.text(temp, -0.5, '(a)', fontsize=22, ha='center')
plt.legend()

plt.subplot(2, 2, 2)
cdf_gcc = data_array_rebuf[:, 0]
cdf_ars = data_array_rebuf[:, 1]
cdf_con = data_array_rebuf[:, 2]
cdf_new = data_array_rebuf[:, 3]
list = np.array(range(len(cdf_gcc)))
list = list / len(list)
plt.plot(cdf_gcc, list, linestyle=':', label="GCC")
plt.plot(cdf_ars, list, linestyle='--', label="ARS")
plt.plot(cdf_con, list, linestyle='-.', label="Concerto")
plt.plot(cdf_new, list, linestyle='-', label="本发明")
# plt.xlim(-10, 5)
# plt.ylim(0.0, 1.0)
plt.xlabel("卡顿率（%）")
plt.ylabel("累计概率")
plt.title("卡顿 CDF曲线图")
max = np.max(data_array_rebuf)
min = np.min(data_array_rebuf)
temp = min+(max-min)/2
plt.text(temp, -0.5, '(b)', fontsize=22, ha='center')
plt.legend()

plt.subplot(2, 2, 3)
cdf_gcc = data_array_rtt[:, 0]
cdf_ars = data_array_rtt[:, 1]
cdf_con = data_array_rtt[:, 2]
cdf_new = data_array_rtt[:, 3]
list = np.array(range(len(cdf_gcc)))
list = list / len(list)
plt.plot(cdf_gcc, list, linestyle=':', label="GCC")
plt.plot(cdf_ars, list, linestyle='--', label="ARS")
plt.plot(cdf_con, list, linestyle='-.', label="Concerto")
plt.plot(cdf_new, list, linestyle='-', label="本发明")
# plt.xlim(-10, 5)
# plt.ylim(0.0, 1.0)
plt.xlabel("平均延迟（s）")
plt.ylabel("累计概率")
plt.title("时延 CDF曲线图")
max = np.max(data_array_rtt)
min = np.min(data_array_rtt)
temp = min+(max-min)/2
plt.text(temp, -0.5, '(c)', fontsize=22, ha='center')
plt.legend()

plt.subplot(2, 2, 4)
cdf_gcc = data_array_send[:, 0]
cdf_ars = data_array_send[:, 1]
cdf_con = data_array_send[:, 2]
cdf_new = data_array_send[:, 3]
list = np.array(range(len(cdf_gcc)))
list = list / len(list)
plt.plot(cdf_gcc, list, linestyle=':', label="GCC")
plt.plot(cdf_ars, list, linestyle='--', label="ARS")
plt.plot(cdf_con, list, linestyle='-.', label="Concerto")
plt.plot(cdf_new, list, linestyle='-', label="本发明")
# plt.xlim(-10, 5)
# plt.ylim(0.0, 1.0)
plt.xlabel("视频码率（kb/s）")
plt.ylabel("累计概率")
plt.title("视频码率 CDF曲线图")
max = np.max(data_array_send)
min = np.min(data_array_send)
temp = min+(max-min)/2
plt.text(temp, -0.5, '(d)', fontsize=22, ha='center')
plt.legend()

fig.tight_layout()
plt.show()
