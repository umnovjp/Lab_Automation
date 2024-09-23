# -*- coding: utf-8 -*-
"""
Spyder Editor

Scripts plots log plot of tek0034.csv file located in the same folder

This is a temporary script file."""

import numpy as np
import matplotlib.pyplot as plt

w1, s1 = np.loadtxt("./tek0034.csv", skiprows=21, delimiter=",", unpack=True)
plt.rcParams['agg.path.chunksize']=150
plt.semilogy(w1,s1)