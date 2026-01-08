class Controller:
    def __init__(self, view, model=None):
        self.view = view
        
        try:
            if self.view.filename_var.get() != '':
               import model
               self.model = model.Model(self.view.filename_var.get())       
            else:
                raise ValueError("No file selected Dave")

            # show a success message
            self.model.show_success(self.model.filename_var.get())
        except Exception as e:
            self.view.show_error(str(e))