"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 16:09
File : traffic_control.py
Description :
https://blog.csdn.net/xiaoyu_750516366/article/details/103041138
https://www.runoob.com/python/att-string-format.html
"""
import time
import subprocess
import numpy as np
import datetime


def cmd(command):
    subp = subprocess.Popen(command, shell=True)


def load_trace(trace_file):
    r = "sudo tc qdisc add dev ens33 root tbf rate 10mbit limit 64k burst 4k"
    print(r)
    cmd(r)
    # latency参数确定了一个包在TBF中等待传输的最长等待时间。
    # burst 缓冲区大小，在Intel体系上，10Mbit/s的速率需要至少10k字节的缓冲区才能达到期望的速率。
    # 导入trace数据
    Bandwidthdata = np.loadtxt(trace_file, dtype=np.float32)

    len_data = min(600, Bandwidthdata.shape[0])
    for row in range(len_data):
        i = Bandwidthdata[row, 1]  # 带宽数据
        # j = Bandwidthdata[row,0] #时间数据
        r = "sudo tc qdisc change dev ens33 root tbf rate " + '{:.4f}'.format(i) + "mbit limit 64k burst 4k"
        cmd(r)  # 执行改变带宽的命令
        record = datetime.datetime.now()
        print(record.strftime('%H:%M:%S ') + '{:>4d}'.format(row) + ' ' + r)
        time.sleep(0.5)  # 等待0.5秒时间
    # 删除限制带宽的队列
    cmd("sudo tc qdisc del dev ens33 root")


if __name__ == '__main__':
    trace_file = './cooked_traces/trace_216826_http---www.amazon.com'
    load_trace(trace_file)
