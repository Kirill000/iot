from main_app import MainApp

class Bootstrap:
    @staticmethod
    def initEnvironment():
        app = MainApp()
        app.mainloop()