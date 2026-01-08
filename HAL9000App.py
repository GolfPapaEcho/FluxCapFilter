import tkinter as tk
from model import Model
from view import View
from controller import Controller


class App(tk.Tk):
    def __init__(self, width, height, title=None):
        super().__init__()

        self.title('HAL9000')
        self.iconbitmap('C:/Users/gpe02/OneDrive/Pictures/Screenshots/HAL9000.ico')
        #print(self.geometry())
        self.geometry(newGeometry='550x400+100+100')
         
        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(view)

        # set the controller to view
        view.set_controller(controller)

       


if __name__ == '__main__':
    app = App(300, 200, "HAL9000")
    app.mainloop()