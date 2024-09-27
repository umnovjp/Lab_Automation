# -*- coding: utf-8 -*-
"""
Spyder Editor

power_split2, power_split is a list
power_array is numpy.ndarray
power is str
length of power_split2 is 1 but length of power_split is 551

This is a temporary script file.
"""
import pyvisa as visa
rm=visa.ResourceManager()
rm.list_resources()
print(rm.visalib.library_path)
Instr19=rm.open_resource('GPIB0::19::INSTR')
Instr19.query('*IDN?')
Usb0=rm.open_resource('USB0::0x0B5B::0xFFF9::815093_146_11::INSTR')
Usb0.timeout=3000
Instr19.timeout=3000
Usb0.query('*IDN?')
Usb0.query('acpower:bandwidth:adjacent?')
Usb0.query('chpower:state?')
Usb0.query('frequency:center?')
Usb0.query('frequency:sigstandard:name?')
Usb0.query('frequency:span?')
Usb0.query('frequency:start?')
Usb0.query('frequency:stop?')
Usb0.write('frequency:center 2400000000')
Instr19.query('freq?')
Instr19.query('freq 2.115000000000E+09')
Instr19.write('power 10')
power=Usb0.query("trace:data?")
print(power)
import numpy as np
import matplotlib.pyplot as plt
power_split=power.split(',')
power_split2=power.split(' ')
power_split.pop(0)
power_split.pop(550)
power_array=np.array(power_split)
print(power_array)
plt.plot(power_split)
plt.show()
print(power_split)
print(float(power_split[0])
exec("for x in range(len(power_split)): print(float(power_split[x]))")
exec("for x in range(len(power_split)): power_list.append(float(power_split[x]))")
print(type(power_split[0]))
print(len(power_split))

fp=open('power_array.txt', "w")
fp.write(power)
fp.close()

fp-open("tek0034.csv")
content=fp.read(1000)
fp.close()
print(content)

w1, s1 = np.loadtxt("tek0034.csv", skiprows=21, delimiter=",", unpack=True)
plt.rcParams['agg.path.chunksize']=500
plt.semilogy(w1,s1)