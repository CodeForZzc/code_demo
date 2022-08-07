"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 15:53
File : pb_to_tflite.py
Description : 将pb模型转换为tflite模式
"""
import tensorflow as tf

# 把pb文件路径改成自己的pb文件路径即可
path = "./frozen_model_cnn.pb"

# 如果是不知道自己的模型的输入输出节点，建议用tensorboard做可视化查看计算图，计算图里有输入输出的节点名称
inputs = ["actor/InputData/X"]
outputs = ["actor/FullyConnected_1/Softmax"]
# 转换pb模型到tflite模型
converter = tf.lite.TFLiteConverter.from_frozen_graph(path, inputs, outputs)

# 在底层，通过将参数（即神经网络权重）的精度从训练时的32位浮点表示降低到更小、更高效的8位整数表示来运行优化（也称为量化）。
# converter.post_training_quantize = True

# 保存一个在tflite中一些无法转换的原模型参数
converter.allow_custom_ops = True

tflite_model = converter.convert()

# yolov3-tiny_160000.tflite这里改成自己想要保存tflite模型的地址即可
open("./frozen_model_cnn.tflite", "wb").write(tflite_model)


