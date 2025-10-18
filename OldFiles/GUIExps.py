# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 10:44:13 2025

@author: Mike G. Hale
Tkinter experiments!
"""
from tkinter import *
from tkinter import filedialog
import pandas as pd

class HAL9000(Tk):
    def __init__(self):
        super().__init__()
        
        #title, icon, size
        self.title("HAL9000")
        self.iconbitmap('C:/Users/gpe02/OneDrive/Pictures/Screenshots/HAL9000.ico')
        self.geometry('700x400')
        
        #Create widgets
        self.your_label = Label(self, text = "I'm sorry Jonathan, there is a fault in the AE35 unit.",
                                font=("Courier New", 12), bd=1, relief="sunken")
        self.your_label.pack(pady=20)
        
        
        self.your_button = Button(self, text="Open File", command=self.file_data)
        self.your_button.pack(pady=20) 
    
    
    
    
    #create popup f()
    def file_data(self):
        self.file_data = filedialog.askopenfilename(initialdir="C:/ti/Sensing Solutions EVM GUI-1.10.0/PC GUI/",
                                                            title="Select a file Jonathan",
                                                            filetypes=(("csv files", "*.csv"),("All Files", "*.*")))
        if self.file_data:
            #Open and read the file into pandas
            df = pd.read_csv(self.file_data)
    
    
#define and instantiate the app
app = HAL9000()
app.mainloop()


