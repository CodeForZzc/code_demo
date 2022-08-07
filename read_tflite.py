"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 15:50
File : read_tflite.py.py
Description : 读取tflite模型文件
"""
import tensorflow as tf
import numpy as np

InputSize = 300
S_INFO = 6
S_LEN = 8
MIN_BIT_RATE = 300
MAX_BIT_RATE = 8000

bitrate = 800
buffer_size = 1.0
received_bit_rate = 680
delay = 0.0029
packet_loss_rate = 0.0133
nack_sent_count = 1.0

state = np.zeros((S_INFO, S_LEN))
for i in range(8):
    state = np.roll(state, -1, axis=1)

    state[0, -1] = 2 * (bitrate - (MIN_BIT_RATE + MAX_BIT_RATE) / 2) / float(
        MAX_BIT_RATE - MIN_BIT_RATE)  # last quality, kilo bits / s
    state[1, -1] = 2 * (1.0 - buffer_size - 0.5)
    state[2, -1] = 2 * (received_bit_rate - (MAX_BIT_RATE + MIN_BIT_RATE) / 2) / float(
        MAX_BIT_RATE - MIN_BIT_RATE)  # kilo bits / s
    state[3, -1] = 2 * (np.log10(delay) / 4 + 0.5)  # 1 sec
    state[4, -1] = 2 * (np.log10(packet_loss_rate) / 4 + 0.5)  # packet_loss_rate
    state[5, -1] = np.log10(float(nack_sent_count) + 1) - 1  # number of nack sent

print(state)

def test_tflite(input_test_tflite_file):
    interpreter = tf.lite.Interpreter(model_path=input_test_tflite_file)
    tensor_details = interpreter.get_tensor_details()
    for i in range(0, len(tensor_details)):
        # print("tensor:", i, tensor_details[i])
        interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    print("=======================================")
    print("input :", str(input_details))
    output_details = interpreter.get_output_details()
    print("ouput :", str(output_details))
    print("=======================================")

    state = np.zeros(48)

    interpreter.set_tensor(input_details[0]['index'], state.reshape(1, 6, 8).astype(np.float32))
    # 注意注意，我要调用模型了
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)
    print(np.argmax(output_data))
    print("test_tflite finish!")

intput_tflite_file = "./frozen_model_cnn.tflite"
test_tflite(intput_tflite_file)
