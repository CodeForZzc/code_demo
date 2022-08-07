"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 16:20
File : multi_python.py
Description : 同时运行多个Python文件
"""
import threading
import time
import os

flag = 1
rtc_port = 13991
abr_port = 13950
name = 'data_41_'
devices = '103.236.121.28:5585'


def log_cpu():
    cmd1 = 'python log_cpu.py ' + str(flag) + ' ' + str(rtc_port) + ' ' + str(abr_port) + ' ' + str(name) + ' ' + str(
        devices)
    os.system(cmd1)
    # print(cmd1)


def haima_start():
    cmd2 = 'python start.py'
    os.system(cmd2)


def log_gpu_mem():
    cmd3 = 'python log_gpu_mem.py ' + str(flag) + ' ' + str(rtc_port) + ' ' + str(abr_port) + ' ' + str(
        name) + ' ' + str(devices)
    os.system(cmd3)


def logcat_bitrate():
    cmd3 = 'python logcat.py ' + str(flag) + ' ' + str(rtc_port) + ' ' + str(abr_port) + ' ' + str(name) + ' ' + str(
        devices)
    os.system(cmd3)


if __name__ == '__main__':
    log_cpu_thread = threading.Thread(target=log_cpu)
    haima_start_thread = threading.Thread(target=haima_start)
    log_gpu_mem_thread = threading.Thread(target=log_gpu_mem)
    logcat_bitrate_thread = threading.Thread(target=logcat_bitrate)

    log_cpu_thread.start()
    haima_start_thread.start()
    log_gpu_mem_thread.start()
    logcat_bitrate_thread.start()
