# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 20:31:15 2025

@author: gpe02
"""
import csv
import pandas as pd
import numpy

def get_data(filename):
    cap_data = pd.read_csv(filename)
    cap_data = cap_data['DATA0_pF'].values
    rowsn = len(cap_data)
    first10 = cap_data[:3]
    print(first10)
    print(rowsn)

get_data(r"C:\ti\Sensing Solutions EVM GUI-1.10.0\PC GUI\testdata.csv")