"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 15:46
File : plot.py
Description : 用于画图
"""
import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig = plt.figure(figsize=(12, 6))
plt.rcParams.update({"font.size": 20})

# 一元二次函数图像
x = np.arange(0, 0.5, 0.001)
y = -2 * x * x + 2 * x + 1
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("")
plt.plot(x, y, label='data')

plt.legend()
plt.show()
# plt.set_xlim(0, 100)
# plt.set_ylim(0, 5500)