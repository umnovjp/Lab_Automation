# -*- coding: utf-8 -*-
"""
Created on Sep 21 18:08:23 2024
Author: Alex
"""

import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time

power_list850 = []
power_list852 = []
power_axis = []
rm=visa.ResourceManager()
rm.list_resources()

Instr28 = rm.open_resource('GPIB0::28::INSTR')
Usb0  = rm.open_resource('USB0::0x0B5B::0xFFF9::1246083_1832_24::INSTR')
Usb0.timeout = 3000
Instr28.timeout = 3000

# generator = SML02(Instr28)
Instr28.write('freq 0.848000000000E+09')
Instr28.write('power 10')
print(Instr28.query('*IDN?'))
# generator.freq
print(Usb0.query('*IDN?'))

power850=Usb0.query("trace:data?")
Instr28.write('power 20')
power_split850=power850.split(',')
power_split850.pop(0)
power_split850.pop(len(power_list850)-1)
power_array850 = np.array(power_split850)
fp = open('power_array848.txt', "w")
fp.write(power850)
fp.close()
Instr28.write('freq 0.852000000000E+09')
Instr28.write('power 20')
time.sleep(5)
Instr28.write('freq 0.852000000000E+09')
# generator.freq = 852000000 # this line does not do what it is expected to do
power852=Usb0.query("trace:data?")
power_split852=power852.split(',')
power_split852.pop(0)
power_split852.pop(len(power_list852)-1)
power_array852 = np.array(power_split852)
time.sleep(5)
# Instr28.write('power 0.1')
Instr28.query('freq?')
freqStart = Usb0.query('frequency:start?')
freqStop = Usb0.query('frequency:stop?')

for x in range(len(power_split850)):
    power_axis.append((0.000000001)*float(freqStart)+0.000000001*x*(float(freqStop)-float(freqStart))/len(power_split850))
    power_list850.append(float(power_split850[x]))
    power_list852.append(float(power_split852[x]))
    

plt.plot(power_axis, power_list850, label='850')
plt.plot(power_axis, power_list852, label='852')
plt.xlim(0.82, 0.88)
plt.show()

print(power850)

# analyzer = MS2721E(Usb0)
# print('IDN= {}'.format(analyzer.idn))
# print(analyzer.saveData)

Instr28.close()
Usb0.close()