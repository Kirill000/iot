from MainApp import MainApp

class Bootstrap:
    @staticmethod
    def initEnvironment():
        app = MainApp()
        app.mainloop()