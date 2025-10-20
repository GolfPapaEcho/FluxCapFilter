#generate HAL9000 view

import tkinter as tk
from tkinter import Button, Label, ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
#set controller
        self.controller = None        
#create widgets
        
        
        #self.filename_var = tk.StringVar()
        #Create widgets
        self.your_label = Label(self, text = "I'm sorry Dave, there is a fault in the AE35 unit.",
                                font=("Courier New", 12), bd=1, relief="sunken")
        self.your_label.pack(pady=20)
        
        
        self.your_button = Button(self, text="Open File", command=self.get_file_data)
        self.your_button.pack(pady=20) 
    def get_file_data(self):
        self.file_data = fd.askopenfilename(initialdir="C:/ti/Sensing Solutions EVM GUI-1.10.0/PC GUI/",
                                                            title="Select a file Dave",
                                                            filetypes=(("csv files", "*.csv"),("All Files", "*.*")))           
          
    def set_controller(self, controller):
        self.controller = controller
    
    
 
       


# Process button


#def process_button_clicked(self):
    #if self.controller:
     #   self.controller.process(self.file_data)
#process_button.pack(expand=True)           
   
    
   
    




