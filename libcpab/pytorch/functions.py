# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:01:52 2018

@author: nsde
"""

#%%
import torch
from .interpolation import interpolate

#%%
def to(x):
    return torch.Tensor(x)

#%%
def type():
    return [torch.Tensor]

#%%
def pdist(mat):
    norm = torch.sum(mat * mat, 1)
    norm = torch.reshape(norm, (-1, 1))
    D = norm - 2*mat.mm(mat.t()) + norm.t()
    return D

#%%
def sample_transformation(d, n_sample=1, mean=None, cov=None):
    mean = torch.zeros(d,dtype=torch.float32) if mean is None else mean
    cov = torch.eye(d,dtype=torch.float32) if cov is None else cov
    distribution = torch.distributions.MultivariateNormal(mean, cov)
    return distribution.sample((n_sample,))

#%%
def identity(d, n_sample=1, epsilon=0):
    assert epsilon>=0, "epsilon need to be larger than 0"
    return torch.zeros(n_sample, d, dtype=torch.float32) + epsilon

#%%
def uniform_meshgrid(ndim, domain_min, domain_max, n_points):
    lin = [torch.linspace(domain_min[i], domain_max[i], n_points[i]) for i in range(ndim)]
    mesh = torch.meshgrid(lin)
    grid = torch.cat([g.reshape(1,-1) for g in mesh], dim=0)
    return grid