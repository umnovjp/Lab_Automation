# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:19:29 2024

@author: Remote
"""

from __future__ import print_function
import pyvisa as visa
rm=visa.ResourceManager()
rm.list_resources()
print(rm.visalib.library_path)
Instr19=rm.open_resource('GPIB0::19::INSTR')
Instr19.query('*IDN?')
Instr19.timeout=3000

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import display, clear_output
import numpy as np
from matplotlib.pyplot import *

widgets.Text(value='Text', placeholder='Type...', description='TextArea', disabled = False)
beta_slider=widgets.FloatSlider(value=2.355, min=0.7, max=4.0, step=0.001, description='beta', readout_format='.3f')
update_button=widgets.Button(description='Update', disabled = False, button_style='success', tooltip='button', icon = '')
def update_button_clicked(b):
    x=beta_slider.value
update_button.on_click(update_button_clicked)
display(beta_slider)