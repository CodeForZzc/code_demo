"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 16:05
File : read_trace.py
Description : 统计网络trace的带宽分布情况
"""
import os
import numpy as np

TRACE_Dir = './Pensieve-traces/train_sim_traces/'
FRAME_NUM_LIMIT = 3600

filelist =  os.listdir(TRACE_Dir)

all_out = [[]]
all_mean = []
cnt_0_1 = 0
cnt_1_2 = 0
cnt_2_3 = 0
cnt_3_4 = 0
cnt_4_5 = 0
cnt_else = 0
cnt_num = 0
for ifile in filelist:
    out = []
    with open(str(TRACE_Dir + ifile), 'rb') as f:
        for line in f:
            # print(float((line.split()[0])))  # 不能直接变int型
            out.append(float((line.split()[-1])))
    all_mean.append(np.mean(out[:]))
    all_out.append(out)
    cnt_num += 1
    if all_mean[-1] <= 1:
        cnt_0_1 += 1
    elif all_mean[-1] <= 2:
        cnt_1_2 += 1
    elif all_mean[-1] <= 3:
        cnt_2_3 += 1
    elif all_mean[-1] <= 4:
        cnt_3_4 += 1
    elif all_mean[-1] <= 5:
        cnt_4_5 += 1
    else:
        cnt_else += 1

print(all_mean[:])
print('cnt_0_1:' + str(cnt_0_1))
print('cnt_1_2:' + str(cnt_1_2))
print('cnt_2_3:' + str(cnt_2_3))
print('cnt_3_4:' + str(cnt_3_4))
print('cnt_4_5:' + str(cnt_4_5))
print('cnt_else:' + str(cnt_else))
print('cnt_num:' + str(cnt_num))
