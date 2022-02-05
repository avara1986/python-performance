from python_performance.main import my_function


class TimeSuite:
    def setup(self):
        self.lista = [i for i in range(500)]

    def time_my_function(self):
        my_function()
