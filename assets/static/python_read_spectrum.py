# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:44:53 2024

save spectrum diagram 

@author: Remote
"""

import pyvisa as visa
rm=visa.ResourceManager()
rm.list_resources()
Instr19=rm.open_resource('GPIB0::19::INSTR')
Usb0=rm.open_resource('USB0::0x0B5B::0xFFF9::815093_146_11::INSTR')
Instr19.write('freq 2.355000000000E+09')
power=Usb0.query("trace:data?")
import numpy as np
import matplotlib.pyplot as plt
power_list=[]
power_split=power.split(',')
power_split.pop(0)
power_split.pop(550)
for x in range(len(power_split)): 
    power_list.append(float(power_split[x]))
plt.plot(power_list)
plt.show()
fp=open('power_array.txt', "w")
fp.write(power)
fp.close()
Instr19.close()
Usb0.close()