from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets

w=widgets.IntSlider()
display(w)

def f(x):
    return x**2.

interact(f,x = 10)

def f_show(x):
    print(x)

interact (f_show,x = ['Apple', 'Orange', 'Strawberry'])

