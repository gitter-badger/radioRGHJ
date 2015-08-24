#! /usr/bin/env python
import numpy as np

k_b = 1.380658e-16

def Tsky(nu):
    return 237 * (nu/.150)**-2.5

def sense(d, N, nu, B=100e6, t=3600):
    return 2 * 1.22**2 * np.pi / (4 *np.log(2)) *  k_b * Tsky(nu) / (N * d**2 * np.sqrt(B*t) * 1e-23)
#    return 2 * k_b * Tsky(nu) / (N * d**2 * np.sqrt(B*t) * 1e-23)
