"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 16:22
File : read_data_from_logcat.py
Description : 从Logcat等文件中读取相关信息
"""
import os
import time
import numpy as np

flag = 0
name = 'data_9_'
dir = './0720/9/'

temp1 = dir + 'client_file.txt'
temp2 = dir + name + 'all_cpu.txt'
temp3 = dir + name + 'all_gpu.txt'
temp4 = dir + name + 'rtc_mem.txt'
temp5 = dir + name + 'abr_mem.txt'
temp6 = dir + name + 'logcat.txt'

fps = []
jank = []
bigjank = []
cpu_rtc = []
cpu_abr = []
gpu = []
mem_rtc = []
mem_abr = []
set_bitrate = []
recv_bitrate = []


def run():
    file_in = open(temp1, 'r')  # 打开输出的文件（临时使用的）
    for line in file_in:
        if ':' in line:  # 这里的单位是bits
            strings = line[:].split('\t')
            fps.append(float(strings[4]))
            jank.append(float(strings[5]))
            bigjank.append(float(strings[6]))

    file_in = open(temp2, 'r')  # 打开输出的文件（临时使用的）
    for line in file_in:
        if 'org.appspot.apprtc' in line:  # 这里的单位是bits
            strings = line[:].split()
            cpu_rtc.append(float(strings[8]))
        if 'com.example.test' in line:  # 这里的单位是bits
            strings = line[:].split()
            cpu_abr.append(float(strings[8]))

    file_in = open(temp3, 'r')  # 打开输出的文件（临时使用的）
    for line in file_in:
        if '=' not in line and line != '\n':  # 这里的单位是bits
            strings = line[:].split()
            gpu.append(float(strings[0]) / float(strings[1]))

    file_in = open(temp4, 'r')  # 打开输出的文件（临时使用的）
    for line in file_in:
        if 'PSS' not in line and 'TOTAL' in line:  # 这里的单位是bits
            strings = line[:].split()
            mem_rtc.append(float(strings[1]))

    if flag == 1:
        file_in = open(temp5, 'r')  # 打开输出的文件（临时使用的）
        for line in file_in:
            if 'PSS' not in line and 'TOTAL' in line:  # 这里的单位是bits
                strings = line[:].split()
                mem_abr.append(float(strings[1]))

    file_in = open(temp6, 'r', encoding='utf-8')  # 打开输出的文件（临时使用的）
    for line in file_in:
        if flag == 0:
            if 'Set bitrateAdjuster' in line:  # 这里的单位是bits
                strings = line[:].split('::::::')
                set_bitrate.append(float(strings[1].split('K')[0]) * 8)
        else:
            if 'newBitrate:' in line:  # 这里的单位是bits
                strings = line[:].split('newBitrate:')
                set_bitrate.append(float(strings[1]))
        if 'recvBitrate:' in line:  # 这里的单位是bits
            strings = line[:].split(':')
            recv_bitrate.append(float(strings[4].split(',')[0]))

    fps_np = np.array(fps)
    jank_np = np.array(jank)
    bigjank_np = np.array(bigjank)
    cpu_rtc_np = np.array(cpu_rtc)
    cpu_abr_np = np.array(cpu_abr)
    gpu_np = np.array(gpu)
    mem_rtc_np = np.array(mem_rtc)
    mem_abr_np = np.array(mem_abr)
    set_bitrate_np = np.array(set_bitrate)
    recv_bitrate_np = np.array(recv_bitrate)

    print('fps:' + str(np.mean(fps_np)))
    print('jank:' + str(np.mean(jank_np)))
    print('bigjank:' + str(np.mean(bigjank_np)))
    print('cpu_rtc:' + str(np.mean(cpu_rtc_np)))
    print('cpu_abr:' + str(np.mean(cpu_abr_np)))
    print('gpu:' + str(np.mean(gpu_np)))
    print('mem_rtc:' + str(np.mean(mem_rtc_np)))
    print('mem_abr:' + str(np.mean(mem_abr_np)))
    print('set_bitrate:' + str(np.mean(set_bitrate_np)))
    print('recv_bitrate:' + str(np.mean(recv_bitrate_np)))

    print('\n')
    print(np.mean(fps_np))
    print(np.mean(jank_np))
    print(np.mean(bigjank_np))
    print(np.mean(cpu_rtc_np))
    print(np.mean(cpu_abr_np))
    print(np.mean(gpu_np))
    print(np.mean(mem_rtc_np))
    print(np.mean(mem_abr_np))
    print(np.mean(set_bitrate_np))
    print(np.mean(recv_bitrate_np))

    print('\n')
    print(len(fps_np))
    print(len(jank_np))
    print(len(bigjank_np))
    print(len(cpu_rtc_np))
    print(len(cpu_abr_np))
    print(len(gpu_np))
    print(len(mem_rtc_np))
    print(len(mem_abr_np))
    print(len(set_bitrate_np))
    print(len(recv_bitrate_np))


def main():
    run()


if __name__ == '__main__':
    main()
