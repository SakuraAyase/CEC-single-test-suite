from cec2019comp100digit import cec2019comp100digit
from functions import *


class cec2019:

    num_of_func = 10

    def __init__(self, func_id):

        self.bench = cec2019comp100digit
        self.func_id = func_id
        if (self.func_id == 1):
            self.max = 8192
            self.min = -8192
            self.D = 9

        elif (self.func_id == 2):
            self.max = 16384
            self.min = -16384
            self.D = 16
        elif (self.func_id == 3):
            self.max = 4
            self.min = -4
            self.D = 18
        elif (self.func_id >= 4 and self.func_id <= 10):
            self.max = 100
            self.min = -100
            self.D = 10
        self.MAXFES = self.D * 10000
        self.N = 50
        self.bench.init(self.func_id, self.D)


    def get_Parameters(self):
        map = {'MAX':self.max, 'MIN':self.min, 'N':self.N, 'D':self.D, 'MAXFES':self.MAXFES}
        return map

    def func(self, x):
        return self.bench.eval(x)

    def end(self):
        self.bench.end()