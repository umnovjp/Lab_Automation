# -*- coding: utf-8 -*-
"""
Spyder Editor

plt.semilogy(w1,s1)

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

w1, s1 = np.loadtxt("./tek0034.csv", skiprows=21, delimiter=",", unpack=True)
plt.rcParams['agg.path.chunksize']=500
plt.xlim(-0.005,0.005)
plt.ylim(-1,1)
plt.plot(w1,s1)