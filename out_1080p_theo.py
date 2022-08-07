"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 17:49
File : out_1080p_theo.py
Description : 将mkv文件转换成qp=0的1080p参考文件
"""
import os

Video_Dir = "./example_file/video_yuv_25/"
Out_Dir = "./example_file/video_all_1080p_theo/"  # 文件地址

FPS = 25  # 帧数
GOP = 125  # GOP大小

filelist = os.listdir(Video_Dir)  # 需要编码的文件

for ifile in filelist:
    mkvfile = Video_Dir + ifile  # 读取的mkv文件
    mp4file = Out_Dir + str(ifile) + '.mp4'  # 生成的h264文件

    # 1080p
    cmd = 'ffmpeg -v error -s 1920*1080 -r 25 -i ' + mkvfile + ' -c:v libx264 -qp 0 -r ' + str(FPS) + ' -g ' + str(
        GOP) + ' -bf 0 ' + '-y ' + mp4file

    print(cmd)
    os.system(cmd)
