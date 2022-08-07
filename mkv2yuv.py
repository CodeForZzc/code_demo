"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 16:17
File : mkv2yuv.py
Description : mkv格式视频通过命令行转yuv格式
"""
import os

Video_Dir = "./new_mkv/"  # 原视频地址
Out_Dir = "./new_yuv/"  # 原视频地址
filelist = os.listdir(Video_Dir)  # 需要编码的文件

for ifile in filelist:
    mkvfile = Video_Dir + ifile  # 读取的yuv文件
    yuvfile = Out_Dir + ifile
    cmd = 'ffmpeg -v error -i ' + mkvfile + ' -y ' + yuvfile + '.yuv'

    print(cmd)

    os.system(cmd)
