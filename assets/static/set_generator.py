# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:19:29 2024

@author: Remote
"""

import pyvisa as visa
rm=visa.ResourceManager()
rm.list_resources()
print(rm.visalib.library_path)
Instr19=rm.open_resource('GPIB0::19::INSTR')
Instr19.query('*IDN?')
Instr19.timeout=3000

from IPython.display import display, clear_output
import numpy as np
from matplotlib.pyplot import *

widgets.Text(value='Text', placeholder='Type...', description='TextArea', disabled = False)
