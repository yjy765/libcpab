# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:01:52 2018

@author: nsde
"""

#%%
import tensorflow as tf
import tensorflow_probability as tfp
from .interpolation import interpolate

#%%
def to(x):
    return tf.cast(x, dtype=x.dtype)

#%%
def type():
    return [tf.python.ops.variables.RefVariable,
            tf.python.framework.ops.Tensor]

#%%
def pdist(mat):
    norm = tf.reduce_sum(mat * mat, 1)
    norm = tf.reshape(norm, (-1, 1))
    D = norm - 2*tf.matmul(mat, tf.transpose(mat)) + tf.transpose(norm)
    return D

#%%
def sample_transformation(d, n_sample=1, mean=None, cov=None):
    mean = tf.zeros((d,), dtype=tf.float32) if mean is None else mean
    cov = tf.eye(d, dtype=tf.float32) if cov is None else cov
    distribution = tfp.distributions.MultivariateNormalFullCovariance(mean, cov)
    return distribution.sample(n_sample)

#%%
def identity(d, n_sample=1, epsilon=0):
    assert epsilon>=0, "epsilon need to be larger than 0"
    return tf.zeros((n_sample, d), dtype=tf.float32) + epsilon

#%%
def uniform_meshgrid(ndim, domain_min, domain_max, n_points):
    lin = [tf.linspace(tf.cast(domain_min[i], tf.float32), 
           tf.cast(domain_max[i], tf.float32), n_points[i]) for i in range(ndim)]
    mesh = tf.meshgrid(*lin[::-1])
    grid = tf.concat([tf.reshape(array, (1, -1)) for array in mesh[::-1]], axis=0)
    return grid