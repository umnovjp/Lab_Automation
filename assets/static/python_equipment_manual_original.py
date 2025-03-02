"""
Created on Dec 21 18:08:23 2024
Author: Alex
"""

class LabInstrument(object):
    def __init__(self,visa_instrument):
        self.instrument = visa_instrument
    @property # @ is decorator sign
    def idn(self):
        """
        return self.instrument.query('"*IDN?"')
        """
        try:
            self._idn=self.instrument.query('*IDN?') #the leading # indicates private attribute
            return self._idn
        except ZeroDivisionError:
            print("Cannot divide by zero!")
class SML02(LabInstrument):
    def __init__(self,visa_instrument):
        super().__init__(visa_instrument) # super allows us to call the method of parent class
    @property
    def freq(self):
        return float(self.instrument.query('freq?'))
    @freq.setter
    def freq(self,freq):
        self.instrument.write('freq 0.85000000000E+09')

class MS2721E(LabInstrument):
    def __init__(self,visa_instrument):
        super().__init__(visa_instrument)
    @property
    def saveData(self):
        power=Usb0.query("trace:data?")
        power_split=power.split(',')
        power_split.pop(0)
        power_split.pop(len(power_list)-1)
        power_array = np.array(power_split)
        fp = open('power_array.txt', "w")
        fp.write(power)
        fp.close()
        freqStart = Usb0.query('frequency:start?')
        freqStop = Usb0.query('frequency:stop?')
        for x in range(len(power_split)):
            power_axis.append((0.000000001)*float(freqStart)+0.000000001*x*(float(freqStop)-float(freqStart))/len(power_split))
            power_list.append(float(power_split[x]))
        
        plt.plot(power_axis,power_list, label='2351')
        plt.show()
        return(power_list)
import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plt
import time

power_list = []
power_axis = []
rm=visa.ResourceManager()
rm.list_resources()

Instr28 = rm.open_resource('GPIB0::28::INSTR')
Usb0  = rm.open_resource('USB0::0x0B5B::0xFFF9::1246083_1832_24::INSTR')
Usb0.timeout = 3000
Instr28.timeout = 3000

generator = SML02(Instr28)
print('IDN= {}'.format(generator.idn))
generator.freq
print('Frequency={:f} GHz'.format(generator.freq/1e9))
time.sleep(5)
generator.freq = generator.freq+5000000 # this line does not do what it is expected to do
time.sleep(5)
print('Frequency={:f} GHz'.format(generator.freq/1e9))

analyzer = MS2721E(Usb0)
print('IDN= {}'.format(analyzer.idn))
print(analyzer.saveData)

Instr28.close()
Usb0.close()