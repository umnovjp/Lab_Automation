# -*- coding: utf-8 -*-
"""
Spyder Editor

power_split2, power_split is a list
power_array is numpy.ndarray
power is str
plt.semilogy(w1,s1)
length of power_split2 is 1 but length of power_split is 551

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

w1, s1 = np.loadtxt("./tek0034.csv", skiprows=21, delimiter=",", unpack=True)
plt.rcParams['agg.path.chunksize']=500
plt.xlim(-0.005,0.005)
plt.ylim(-1,1)
plt.plot(w1,s1)