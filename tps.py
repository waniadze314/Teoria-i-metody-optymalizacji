import numpy as np
from sys import stdin
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
class simplex:
    def __init__(self):
        # I_matrix = np.identity(n, dtype = float)
        self.rows = 0
        self.columns = 0
        self.variables_counter = 0
        self.inequations_counter = 0
        self.table = []
        self.init_table = []
        self.base_variables = []
        self.key_row = 0
        self.key_column = 0
        self.key_value = 0

    def get_problem_coefficients(self):
        tmp_eq_row = 1
        tmp_rows, tmp_columns = map(int, input().split())
        self.inequations_counter = tmp_rows
        self.variables_counter = tmp_columns
        self.base_variables = np.zeros((tmp_rows,1))
        for i in range(1,tmp_rows+1):
            self.base_variables[i-1] = tmp_columns + i
        tmp_iden_row = tmp_columns + 1
        self.rows = tmp_rows + 3
        self.columns = tmp_columns + tmp_rows + 2
        equations = []
        for i in range(0,tmp_rows):
            equations.append(list(map(float, input().split())))
        boundaries_coefs = list(map(float, input().split()))
        function_coefs = list(map(float, input().split()))    
        self.table = np.zeros((self.rows, self.columns))
        for eq in equations:
            for i in range(0,tmp_columns):
                self.table[tmp_eq_row][i+1] = eq[i]            
            self.table[tmp_eq_row][tmp_iden_row] = 1
            tmp_iden_row = tmp_iden_row + 1
            tmp_eq_row = tmp_eq_row + 1
        for i in range(0,tmp_rows):
            self.table[i+1][self.columns-1] = boundaries_coefs[i]
        for i in range(0,tmp_columns):
            self.table[0][i+1] = function_coefs[i]

        for c in range(1,self.columns):
            tmp_z = 0
            for r in range(1,self.rows-1):
                tmp_z = tmp_z + self.table[r][0] * self.table[r][c]
            self.table[self.rows-2][c] = tmp_z
            self.table[self.rows-1][c] = self.table[0][c] - self.table[self.rows-2][c]
        self.table[0][0] = self.table[self.rows-1][self.columns-1] = 0
        self.init_table = self.table
        self.calculate_value()
        print(self.table)
        print(self.base_variables)

    def calculate_value(self):
        function_value = 0
        for r in range(1, self.rows-2):
            function_value = function_value + self.table[r][0]*self.table[r][self.columns-1]
        self.table[self.rows-2][self.columns-1] = function_value
        return function_value

    def print_table(self):
        print(self.table)

    def find_pivot(self):
        tmp_column = 1
        tmp_c_val = self.table[self.rows-1][tmp_column]
        for c in range(2, self.columns-1):
            t = self.table[self.rows-1][c]
            if t > tmp_c_val:
                tmp_c_val = t
                tmp_column = c
        tmp_row = 1
        tmp_r_val = self.table[1][self.columns-1]/self.table[1][tmp_column]
        for r in range(2, self.rows-2):
            t = self.table[r][self.columns-1]/self.table[r][tmp_column]
            if t < tmp_r_val:
                tmp_r_val = t
                tmp_row = r
        self.key_column = tmp_column
        self.key_row = tmp_row        
        self.key_value = self.table[tmp_row][tmp_column]
        return
  
    def check_optimality(self):
        for i in range(1,self.columns-1):
            if self.table[self.rows-1][i] > 0:
                return False
        return True
    
    def calculation_iter(self):
        tmp_table = np.copy(self.table)
        self.find_pivot()
        self.table[self.key_row][0] = self.table[0][self.key_column]
        self.base_variables[self.key_row-1] = self.key_column

        for c in range(1, self.columns):
            self.table[self.key_row][c] = tmp_table[self.key_row][c]/self.key_value
        
        for r in range(1, self.rows-2):
            if r != self.key_row:                
                for c in range(1, self.columns):
                    self.table[r][c] = tmp_table[r][c] - ((tmp_table[self.key_row][c] * tmp_table[r][self.key_column])/self.key_value)
        
        for c in range(1,self.columns-1):
            tmp_z = 0
            for r in range(1,self.rows-1):
                tmp_z = tmp_z + self.table[r][0] * self.table[r][c]
            self.table[self.rows-2][c] = tmp_z
            self.table[self.rows-1][c] = self.table[0][c] - self.table[self.rows-2][c]
        f_val = self.calculate_value()
        self.print_table()
        print("Base variables: ", self.base_variables)
        print("Function value: ", f_val)

    def phase_one(self):
        stop = self.check_optimality()
        iteration = 0
        while stop==False:
            self.calculation_iter()
            stop = self.check_optimality()
            iteration = iteration + 1
            print(iteration)
        return iteration

    def phase_two(self):
        return 0

st = simplex()
st.get_problem_coefficients()
st.phase_one()