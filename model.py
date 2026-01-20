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
import csv
from datetime import datetime
from tkinter.messagebox import showinfo
import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk



class Model:
    def __init__(self, filename):
        self.filename = filename
        # Filter requirements.
        self.order = 6
        self.fs = 20.0       # sample rate, Hz
        self.cutoff = 0.1  # desired cutoff frequency of the filter, Hz
        #self.cap_data = pd.read_csv(filename)
        self.cap_data = pd.read_csv(self.filename)
        #eg filename r"C:\ti\Sensing Solutions EVM GUI-1.10.0\PC GUI\testdata.csv"
        self.cap_data = self.cap_data['DATA0_pF'].values
        num_data_points = len(self.cap_data)
        #time_sv creates a vector of the time in ms. For data spaced at 50ms (20Hz).
        time_sv = np.arange(0, (50*num_data_points), 50)

            
        def butter_lowpass(cutoff, fs, order):
            return butter(order, cutoff, fs=fs, btype='low', analog=False)

        def butter_lowpass_filter(cap_data, cutoff, fs, order):
            b, a = self.butter_lowpass(cutoff, fs, order=order)
            y = lfilter(b, a, cap_data)
            return y


    
    
    # Get the filter coefficients so we can check its frequency response.
        b, a = butter_lowpass(self.cutoff, self.fs, self.order)
        
        # Plot the frequency response.
        w, h = freqz(b, a, fs=self.fs, worN=8000)
#plt.subplot(2, 1, 1)
        plt.plot(w, np.abs(h), 'b')
        plt.plot(self.cutoff, 0.5*np.sqrt(2), 'ko')
        plt.axvline(self.cutoff, color='k')
        plt.xlim(0, 0.01*self.fs)
        plt.title("Lowpass Filter Frequency Response")
        plt.xlabel('Frequency [Hz]')
        plt.grid()
        plt.show()
            
        # Filter the data, and plot both the original and filtered signals.
        y = butter_lowpass_filter(self.cap_data, self.cutoff, self.fs, 6) #6th degree = order hence number 6

        plt.subplot(2, 1, 2)
        plt.plot(time_sv, self.cap_data, 'b-', label='data')
        plt.plot(time_sv, y, 'g-', linewidth=2, label='filtered data')
        plt.xlabel('Time [sec]')
        plt.grid()
        plt.legend()

        plt.subplots_adjust(hspace=0.35)
        plt.show()    
        
        #write csv of filtered data
        try:
            now = datetime.now()
            dTString = now.strftime("%d.%m.%Y.%H:%M:%S")
            fileName = "~/Pressure/" + "EfluxCapacitor" + dTString + ".csv"
            with open(fileName, 'w') as f:
                writer = csv.writer(f, delimiter=",", lineterminator="\n")
                writer.writerow(['Time/ms', 'Filtered Capacitance/pF', 'Ca[acitance/pF'])
                for i in range(len(y)):
                    writer.writerow([time_sv, y, self.cap_data])
            f.close()
        except KeyboardInterrupt:
            f.close()
            print('\n', "Exit on Ctrl-C: Good bye!")
        #print(self.cap_data)
    
    def show_success(self, filename):
        message = f'The file {filename} has been processed Dave'     
        showinfo(title='Success', message=message)