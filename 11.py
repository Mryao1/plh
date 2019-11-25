import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
sess = tf.Session()
a = tf.constant(1)
b = tf.constant(2)
print(sess.run(a+b))