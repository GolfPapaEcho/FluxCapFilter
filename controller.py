class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process(self, filename):
        """
        Pass filename to model
        :return:
        """
        try:

            # start the model process
            self.model.process(self.view.file_data)

            # show a success message
            self.view.show_success(f'The file {filename} has been processed Dave')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)