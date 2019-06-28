#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: libraravipandey@gmail.com
"""


#program1
import tensorflow as tf

#declaration of  variable
hello=tf.constant('Hello, Tensorflow ...Basic')
#initialization of tensorflow session
sess=tf.Session()

#printing variable inside session
print(sess.run(hello))

#program2

import tensorflow as tf
sess=tf.Session()
a=tf.constant(1)
b=tf.constant(6)
c=a+b
#print(c) will display you the shape of tensor
print(c)
print(sess.run(c))


#program3
import tensorflow as tf
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b)
divide=a/b
with tf.Session() as sess:
    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))
    print("Divide with variables: %i" % sess.run(divide, feed_dict={a: 6, b: 2}))

