"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 17:06
File : out_bitrate&vmaf.py
Description : 输出bitrate和vmaf文件
"""

import os

Video_Dir = "./example_file/video_yuv_25/"  # 原视频地址
Out_Dir = "./example_file/test/"  # 文件地址
FPS = 25  # 帧数
GOP = 125  # GOP大小

filelist = os.listdir(Video_Dir)  # 需要编码的文件
BITRATE_LIST = range(500, 4500, 50)
BITRATE_LEVELS = len(BITRATE_LIST)  # 码率等级
TEMP_FILE1 = Out_Dir + 'temp1.txt'  # 输出文件txt（临时存在的）
TEMP_FILE2 = 'temp2.txt'  # 输出文件txt（临时存在的）
TEMP_FILE_bitrate = Out_Dir + 'temp_bitrate_'  # 输出文件txt
TEMP_FILE_VMAF = Out_Dir + 'temp_vmaf_'  # 输出文件txt
ref_video_Dir = "./example_file/video_all_1080p_theo/"  # vmaf参考视频地址
i = 0

height = 1080
width = 1920

print('\n')
for ifile in filelist:
    print(i)
    print(ifile)
    i = i + 1

i = 0
for ifile in filelist:

    temp = 25

    for bitrate in range(BITRATE_LEVELS):
        fftp1 = open(TEMP_FILE_bitrate + str(i) + '_' + str(BITRATE_LIST[bitrate]) + '.txt', 'w')
        fftp2 = open(TEMP_FILE_VMAF + str(i) + '_' + str(BITRATE_LIST[bitrate]) + '.txt', 'w')

        mkvfile = Video_Dir + ifile  # 读取的yuv文件
        mp4file = Out_Dir + str(ifile) + '_' + str(i) + '_' + str(BITRATE_LIST[bitrate]) + '.mp4'  # 生成的h264文件

        # 只有ultrafast，才能保证GOP大小为设定大小
        cmd = 'ffmpeg -v error -s 1920*1080 -r ' + str(
            temp) + ' -i ' + mkvfile + ' -c:v libx264 -profile:v main -preset:v ultrafast -r ' + str(
            FPS) + ' -g ' + str(GOP) + ' -bf 0 -x264opts bitrate=' + str(
            int(BITRATE_LIST[bitrate])) + ':vbv-maxrate=' + str(int(BITRATE_LIST[bitrate] * 2)) + ':vbv-bufsize=' + str(
            int(BITRATE_LIST[bitrate] * 2)) + ' -y ' + mp4file

        print(cmd)

        os.system(cmd)

        # 记录帧大小
        os.system('ffprobe -show_frames ' + mp4file + ' >' + TEMP_FILE1)
        file_in = open(TEMP_FILE1, 'r')  # 打开输出的文件（临时使用的）
        iline = 0
        for line in file_in:
            if 'pkt_size' in line:  # 这里的单位是bits
                strings = line[:-1].split('=')
                fftp1.write(strings[1] + '\n')
        file_in.close()
        os.remove(TEMP_FILE1)  # 删除临时文件

        # 记录帧VMAF值
        cmd = 'ffmpeg -hide_banner -r 25 -i ' + mp4file + ' -r 25 -i ' + ref_video_Dir + str(
            ifile) + '.mp4' + ' -lavfi "[0:v]setpts=PTS-STARTPTS[reference];[1:v]setpts=PTS-STARTPTS[distorted];[distorted][reference]libvmaf="log_fmt=xml:log_path=' + './temp2.txt' + ':model_path="D\\\:/ffmpeg/ffmpeg-4.4-essentials_build/vmaf/model/vmaf_v0.6.1.json" -f null -'
        print(cmd)

        os.system(cmd)

        file_in = open(TEMP_FILE2, 'r')  # 打开输出的文件（临时使用的）
        iline = 0
        for line in file_in:
            if 'vmaf' in line:
                if 'frame frameNum' in line:
                    strings = line[:].split('"')
                    fftp2.write(strings[-2] + '\n')
        file_in.close()

        os.remove(TEMP_FILE2)

        # if BITRATE_LIST[bitrate] != 1000:
        #     os.remove(mp4file)  # 删除mp4文件
        os.remove(mp4file)
        fftp1.close()  # 关闭存储文件
        fftp2.close()  # 关闭存储文件
    i = i + 1

for ifile in filelist:
    print(ifile)
