# -*- coding: utf-8 -*-
"""
Created on 16 OCT 2025

@author: Mike G. Hale
with thanks to Warren Weckesser on stack overflow
https://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units

Takes pandas data and applies a lowpass butterworth filter to it
Calculates gradient of cap data to get flow rate
returns capacitance, time, filtered data and dC/dt

"""

import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk



class Model:
    def __init__(self, filename):
        self.cap_data = pd.read_csv(filename)
    
 
        self.cap_data = self.cap_data['DATA0_pF'].values
# %%
        

            

    def butter_lowpass(cutoff, fs, order=5):
        return butter(order, cutoff, fs=fs, btype='low', analog=False)

        def butter_lowpass_filter(data, cutoff, fs, order=5):
            b, a = butter_lowpass(cutoff, fs, order=order)
            y = lfilter(b, a, data)
            return y

    # Filter requirements.
    order = 6
    fs = 20.0       # sample rate, Hz
    cutoff = 0.1  # desired cutoff frequency of the filter, Hz
    
    # Get the filter coefficients so we can check its frequency response.
    b, a = butter_lowpass(cutoff, fs, order)