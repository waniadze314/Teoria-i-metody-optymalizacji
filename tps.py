import numpy as np
from sys import stdin
class simplex:
    def __init__(self):
        # I_matrix = np.identity(n, dtype = float)
        self.rows = 0
        self.columns = 0
        self.in_variable = 'x0'
        self.out_variable = 'x0'
        self.table = []

    def get_problem_coefficients(self):
        tmp_eq_row = 1
        tmp_rows, tmp_columns = map(int, input().split())
        tmp_iden_row = tmp_columns + 1
        self.rows = tmp_rows + 3
        self.columns = tmp_columns + tmp_rows + 2
        equations = []
        for i in range(n):
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
        print(self.table)

    def print_table(self):
        print(self.table)

    def find_pivot(self):
        tmp_column = 1
        tmp_c_val = self.table[self.rows-1][tmp_column]
        for c in range(2, self.columns-2):
            t = self.table[self.rows-1][c]
            if t > tmp_c_val:
                tmp_c_val = t

        tmp_row = 1
        tmp_r_val = self.table[1][self.columns-1]
        for r in range(2, self.rows-3):
            t = self.table[r][self.columns-1]
            if t > tmp_r_val:
                tmp_r_val = t
        print(tmp_r_val)
        print(tmp_c_val)
        return tmp_r_val, tmp_c_val
        # column = 2
        # row = 0
        # tmp_c_value = self.table[1][self.columns-1]/self.table[1][self.columns-1]
        # for r in range(1, self.rows-3):
        #     if self.table[r][self.columns-1]/self.table[r][self.columns-1] > tmp_c_value:
        #         row = r
        # print(row)
        # print(column)
        # return row, column

    def calculation_iter(self):
        self.table = []    

def get_max_value_index(data):
    tmp_value = data[0]
    tmp_value_index = 0
    for i in range(0,data.size):
        if data[i] > tmp_value:
            tmp_value = data[i]
            tmp_value_index = i
    return tmp_value_index

def get_min_value_index(data):
    tmp_value = data[0]
    tmp_value_index = 0
    for i in range(0,data.size):
        if data[i] > tmp_value:
            tmp_value = data[i]
            tmp_value_index = i
    return tmp_value_index

n = 3
m = 3
core = np.array([[1,2,3],[4,5,6],[7,8,9]])
I = np.array([[1,0,0],[0,1,0],[0,0,1]])
cj = np.array([0,0,0,0,0,0])
base = np.concatenate((core,I),axis = 1)
matrix = np.vstack((cj, base))

st = simplex()
st.get_problem_coefficients()
st.find_pivot()
