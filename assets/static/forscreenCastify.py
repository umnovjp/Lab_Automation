# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:05:40 2025

@author: Alexxx
"""

import pyvisa as visa
rm=visa.ResourceManager()
rm.list_resources()
Instr28=rm.open_resource('GPIB0::28::INSTR')
Instr28.query('*IDN?')
Usb0=rm.open_resource('USB0::0x0B5B::0xFFF9::1246083_1832_24::INSTR')
Usb0.timeout=3000
Instr28.timeout=3000
Usb0.query('*IDN?')
Usb0.query('frequency:center?')
Usb0.write('frequency:start 600000000')
Usb0.write('frequency:stop 900000000')
Instr28.write('power 3')
power=Usb0.query("trace:data?")
print(power)
import numpy as np
import matplotlib.pyplot as plt
power_split=power.split(',')

power_split.pop(0)

power_split.pop(len(power_list)-1)
power_list=[]
freqStart = Usb0.query('frequency:start?')
freqStop = Usb0.query('frequency:stop?')
exec("for x in range(len(power_split)): print(float(power_split[x]))")
exec("for x in range(len(power_split)): power_list.append(float(power_split[x]))")
exec("for x in range(len(power_split)): power_axis.append(0.000000001)*float(freqStart)+x*(float(freqStart)-float(freqStop)))")

