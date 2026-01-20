#class Controller:
#    def __init__(self, view, model=None):
#        self.view = view
    
#        try:
           
#            if self.view.filename_var.get() != '':
#                import model
#                print("Controller: File selected is ", self.view.filename_var.get())
#                self.model = model.Model(self.view.filename_var.get())       
                
            # show a success message
#            self.model.show_success(self.model.filename_var.get())
#        except Exception as e:
#            self.view.show_error(str(e))