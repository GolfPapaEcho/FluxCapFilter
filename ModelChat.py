# ...existing code...
# -*- coding: utf-8 -*-
"""
Model for loading capacitance CSV, applying a Butterworth lowpass filter,
computing dC/dt, plotting (optional), and saving filtered results.
"""
import os
import csv
from datetime import datetime
from tkinter.messagebox import showinfo
import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import pandas as pd


class Model:
    def __init__(self, filename, order=6, fs=20.0, cutoff=0.1, save_dir="~/FluxCapFilter", show_plots=True):
        self.filename = filename
        self.order = order
        self.fs = float(fs)
        self.cutoff = float(cutoff)
        self.save_dir = os.path.expanduser(save_dir)
        self.show_plots = show_plots
        self.butter_lowpass = None
        self.butter_lowpass_filter = None
        # Load data
        df = pd.read_csv(self.filename)
        if 'DATA0_pF' in df.columns:
            self.cap_data = df['DATA0_pF'].to_numpy(dtype=float)
        else:
            # fallback: try first numeric column
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) == 0:
                raise ValueError("No numeric columns found in CSV and 'DATA0_pF' not present.")
            self.cap_data = df[numeric_cols[0]].to_numpy(dtype=float)

        self.num_data_points = len(self.cap_data)
        # time vector in seconds (fs samples per second)
        self.time_sv = np.arange(self.num_data_points) / self.fs

        # design filter helpers
        def butter_lowpass(cutoff, fs, order):
            return butter(order, cutoff, fs=fs, btype='low', analog=False)


        def butter_lowpass_filter(cap_data, cutoff, fs, order):
            b, a = butter_lowpass(cutoff, fs, order=order)
            y = lfilter(b, a, cap_data)
            return y

        # Filter design and frequency response
        b, a = butter_lowpass(self.cutoff, self.fs, self.order)
        w, h = freqz(b, a, fs=self.fs, worN=8000)

        # Apply filter
        self.filtered = butter_lowpass_filter(self.cap_data, self.cutoff, self.fs, self.order)

        # Compute gradient (dC/dt) in pF/s
        # Use numpy.gradient which handles endpoints; divide by dt
        dt = 1.0 / self.fs
        self.dC_dt = np.gradient(self.filtered, dt)

        # Plotting (optional)
        if self.show_plots:
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
            ax1.plot(w, np.abs(h), 'b')
            ax1.plot(self.cutoff, 0.5 * np.sqrt(2), 'ko')
            ax1.axvline(self.cutoff, color='k')
            ax1.set_xlim(0, 0.01 * self.fs)
            ax1.set_title("Lowpass Filter Frequency Response")
            ax1.set_xlabel('Frequency [Hz]')
            ax1.grid()

            ax2.plot(self.time_sv, self.cap_data, 'b-', label='raw data')
            ax2.plot(self.time_sv, self.filtered, 'g-', linewidth=2, label='filtered data')
            ax2.plot(self.time_sv, self.dC_dt, 'r-', linewidth=2, label='dC/dt')
            ax2.grid()
            ax2.legend()

            plt.tight_layout()
            plt.show()

        # Save filtered data to CSV
        try:
            os.makedirs(self.save_dir, exist_ok=True)
            now = datetime.now()
            timestamp = now.strftime("%Y%m%d_%H%M%S")
            out_path = os.path.join(self.save_dir, f"EfluxCapacitor_{timestamp}.csv")
            with open(out_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Time_s', 'Filtered_Capacitance_pF', 'Raw_Capacitance_pF', 'dC_dt_pF_per_s'])
                for i in range(self.num_data_points):
                    writer.writerow([
                        float(self.time_sv[i]),
                        float(self.filtered[i]),
                        float(self.cap_data[i]),
                        float(self.dC_dt[i])
                    ])
            self.show_success(out_path)
        except Exception as e:
            # For GUI apps you might prefer showinfo or logging
            showinfo(title='Error', message=f'Failed to save filtered data: {e}')

    def show_success(self, filename):
        message = f'The file {filename} has been processed, Dave'
        showinfo(title='Success', message=message)
# ...existing code...message = f'The file {filename} has been processed, Dave'