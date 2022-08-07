"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 15:46
File : rename.py
Description : 用于批量重命名
"""
import os

File_Dir = "./temp/"  # 原文件地址
filelist = os.listdir(File_Dir)
BITRATE_LIST = range(300, 4300, 50)

i = 0
for ifile in filelist:
    new_name = ifile.split('_')[-1]
    os.rename(os.path.join(File_Dir, ifile), os.path.join(File_Dir, str('temp_bitrate_0_' + str(new_name))))
    i = i + 1
