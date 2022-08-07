"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 17:37
File : read_frame_type.py
Description : 读取视频帧是否为关键帧，需要搭配out_bitrate&vmaf.py使用
"""
import os

TEMP_FILE1 = './test/temp1.txt'

fftp1 = open('./test/read.txt', 'w')

file_in = open(TEMP_FILE1,'r')  # 打开输出的文件（临时使用的）
iline = 0
for line in file_in :
    if 'key_frame' in line :  # 这里的单位是bits
        strings =line[:-1].split('=')
        fftp1.write(strings[1] + '\n')
file_in.close()
# os.remove(TEMP_FILE1)  #删除临时文件