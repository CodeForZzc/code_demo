"""
-*- coding: utf-8 -*-

Author : Zzc
Time : 2022/8/7 16:09
File : tf_test.py
Description : 测试tensorflow安装情况
"""
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

with tf.device('/cpu:0'):
    a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
    b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
with tf.device('/gpu:1'):
    c = a + b

# 注意：allow_soft_placement=True表明：计算设备可自行选择，如果没有这个参数，会报错。
# 因为不是所有的操作都可以被放在GPU上，如果强行将无法放在GPU上的操作指定到GPU上，将会报错。
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
sess.run(tf.global_variables_initializer())
print(sess.run(c))

# -----------------------------------------------------------------------------------------------------------------------
# import tensorflow as tf
#
# inputs = tf.random.normal([32, 10, 8])   # (batch, seq_len, input_size)
# lstm = tf.keras.layers.LSTM(4)  # (units,) # 这里的units等同与Pytorch中的hidden_size
# output = lstm(inputs)
# lstm = tf.keras.layers.LSTM(4, return_sequences=True, return_state=True) # (units, return_sequences, return_state)
# whole_seq_output, final_memory_state, final_carry_state = lstm(inputs)
# print(output.shape)
# print(whole_seq_output.shape)
# print(final_memory_state.shape)
# print(final_carry_state.shape)
#
# -----------------------------------------------------------------------------------------------------------------------
# import tensorflow as tf
# import os
#
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 不显示等级2以下的提示信息
#
# print('GPU', tf.test.is_gpu_available())
#
# a = tf.constant(2.0)
# b = tf.constant(4.0)
# print(a + b)
#
# -----------------------------------------------------------------------------------------------------------------------
# import tensorflow as tf
# mnist = tf.keras.datasets.mnist
#
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0
#
# model = tf.keras.models.Sequential([ tf.keras.layers.Flatten(input_shape=(28, 28)),
#         tf.keras.layers.Dense(128, activation='relu'),
#         tf.keras.layers.Dropout(0.2),
#         tf.keras.layers.Dense(10, activation='softmax') ])
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=5)
# model.evaluate(x_test, y_test, verbose=2)
#
# -----------------------------------------------------------------------------------------------------------------------
# # import tensorflow as tf
# import tensorflow.compat.v1 as tf
# tf.compat.v1.disable_eager_execution()
# with tf.device('/gpu:0'):
#     a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
#     b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
#     c = tf.matmul(a, b)
#     with tf.Session() as sess:
#         print (sess.run(c))
#
# -----------------------------------------------------------------------------------------------------------------------
# import tensorflow as tf
# print(tf.test.is_gpu_available())

