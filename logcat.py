"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 16:24
File : logcat.py
Description : 输出logcat文件信息保存到本地
"""
import os
import sys

# flag = 0
# rtc_port = 8786
# abr_port = 14423
# name = 'data_23_'
# devices = '103.236.121.28:5585'

flag = sys.argv[1]
rtc_port = sys.argv[2]
abr_port = sys.argv[3]
name = sys.argv[4]
devices = sys.argv[5]

def run(flag, rtc_port, abr_port, name, devices):
    cmd = 'adb -s ' + str(devices) + ' shell logcat -c'
    print(cmd)
    os.system(cmd)

    cmd = 'adb -s ' + str(devices) + ' shell logcat > ./' + name + 'logcat.txt'
    print(cmd)
    os.system(cmd)



def main():
    run(flag, rtc_port, abr_port, name, devices)


if __name__ == '__main__':
    main()