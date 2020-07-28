from cec2013_func.functions import *

from functions import *


class cec2013:


    num_of_func = 28
    def __init__(self, func_id):


        self.D = 10
        self.N = 50
        self.bench = CEC_functions(self.D)
        self.func_id = func_id
        self.max = 100
        self.min = -100
        self.MAXFES = self.D * 10000


    def get_Parameters(self):
        map = {'MAX':self.max, 'MIN':self.min, 'N':self.N, 'D':self.D, 'MAXFES':self.MAXFES}
        return map

    def func(self, x):
        return self.bench.Y(x, self.func_id)

    def end(self):
        return 0


if __name__ == "__main__":
    f_num = 2
    cec_functions = cec2013(f_num)

    X = np.ones(30)

    #C Calculations
    # import cic13functions
    # C_Y = np.longdouble(cic13functions.run(str(f_num) + ',' + str(list(X))[1:-1]))

    #Python Calculations
    P_Y = cec_functions.func(X)

    # print('c response:', C_Y )
    print('python response:' , P_Y)
    pass