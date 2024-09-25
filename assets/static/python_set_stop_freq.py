# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:43:36 2024

@author: Remote
"""

import pyvisa as visa
rm=visa.ResourceManager()
rm.list_resources()
Usb0=rm.open_resource('USB0::0x0B5B::0xFFF9::815093_146_11::INSTR')
Usb0.write('frequency:stop 2400000000')
Usb0.close()