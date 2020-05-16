import numpy as np
from sys import stdin
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
class two_phase_simplex:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.number_of_variables = 0
        self.number_of_bounds = 0
        self.table = []
        self.function_coefs = []
        self.base_variables = []
        self.non_base_variables = []
        self.key_row = 0
        self.key_column = 0
        self.key_value = 0
        self.tables_list = []

    def get_problem_coefficients(self, values, bounds):
        self.number_of_bounds = bounds
        input_size = len(values)
        tmp_func = np.zeros(5)
        b_vector = np.zeros(self.number_of_bounds)
        b = 11
        for i in range (0, self.number_of_bounds):            
            b_vector[i] = float(values[b])
            b = b + 7

        for i in range (0,5):
            tmp_func[i] = values[i]        
        for v in range (0,5):
            if tmp_func[self.number_of_variables] == 0:
                break
            else:
                self.number_of_variables = self.number_of_variables + 1
        self.function_coefs = np.array(tmp_func[0:self.number_of_variables])

        input_index = 5
        self.table = np.zeros((self.number_of_bounds+1, self.number_of_variables+1))
        for c in range(1, self.number_of_variables+1):
            self.table[0][c] = (-1)*self.function_coefs[c-1]

        for r in range(1, self.number_of_bounds+1):
            self.table[r][0] = b_vector[r-1]
        for r in range (1,self.number_of_bounds+1):
            if values[input_index + 5] == "≥":
                coef = -1
                self.table[r][0] = coef*self.table[r][0]
            else:
                coef = 1
            
            for c in range(1,self.number_of_variables+1):
                self.table[r][c] = coef*float(values[input_index])
                input_index = input_index + 1
            input_index = input_index + (7 - self.number_of_variables)
        self.base_variables = np.zeros(self.number_of_bounds)
        self.non_base_variables = np.zeros(self.number_of_variables)
        for b in range (0,self.number_of_bounds):
            self.base_variables[b] = b + 1 + self.number_of_variables
        for n in range(0,self.number_of_variables):
            self.non_base_variables[n] = n + 1
        print(self.table)
        # print("Base variables:", self.base_variables)
        # print("Non-base variables: ", self.non_base_variables)
        
    def calculate_value(self):
        function_value = 0
        number_of_all_variables = self.number_of_bounds+self.number_of_variables
        coefs = np.zeros(number_of_all_variables)
        for i in range (0, len(self.base_variables)):
            coefs[int(self.base_variables[i])-1] = self.table[i+1][0]            

        for v in range (0,self.number_of_variables):
            function_value = function_value + coefs[v]*self.function_coefs[v]
        self.table[0][0] = function_value
        return

    def find_minimal_row(self):
        tmp_min = np.inf
        row_index = 1
        for r in range(1,self.number_of_bounds+1):
            val = self.table[r][0]
            if val < 0 and val < tmp_min:
                tmp_min = val;
                row_index = r
        return row_index

    def find_in_variable(self):
        tmp_min = np.inf
        column_index = 0
        for c in range(1,self.number_of_variables+1):
            val = self.table[0][c]
            if val < 0 and val < tmp_min:
                tmp_min=val;
                column_index = c
        if column_index == 0:
            return -1
        else:
            return column_index

        


    def print_table(self):
        print(self.table)

    def find_pivot(self):
        tmp_min = np.inf
        column_index = 1
        for c in range (1,self.number_of_variables+1):
            val = self.table[0][c]
            if val < 0 and val < tmp_min:
                tmp_min = val
                column_index = c
        
        tmp_min = np.inf
        row_index = 1
        for r in range(1, self.number_of_bounds+1):
            if self.table[r][column_index] != 0:
                val =  self.table[r][0]/self.table[r][column_index]
                if val < tmp_min and val > 0:
                    tmp_min = val
                    row_index = r
        self.key_column = column_index
        self.key_row = row_index
        self.key_value = self.table[row_index][column_index]
        return
  
    def check_optimality(self):
        for c in range(1,self.number_of_variables+1):
            if self.table[0][c] < 0:
                return False
        return True
    

    def check_if_permissible(self):
        for r in range (1,self.number_of_bounds+1):
            if self.table[r][0] < 0:
                return False
            else:
                return True

    def phase_one(self):
        if self.check_if_permissible() == True:
            return
        else:
            row = self.find_minimal_row()
            column = self.find_in_variable()
            if column == -1:
                return False
            else:
                while self.check_if_permissible == False:
                    self.phase_iteration()

            

    

    def phase_iteration(self):
        tmp_table = np.copy(self.table)
        self.find_pivot()

        self.table[self.key_row][self.key_column] = 1/self.table[self.key_row][self.key_column]

        for r in range (0,self.number_of_bounds+1):
            if r != self.key_row:
                self.table[r][self.key_column] = (-1)*self.table[r][self.key_column]/self.key_value
        
        for c in range (0,self.number_of_variables+1):
            if c != self.key_column:
                self.table[self.key_row][c] = self.table[self.key_row][c]/self.key_value

        for r in range (0,self.number_of_bounds+1):
            for c in range(0, self.number_of_variables+1):
                if r != self.key_row and c != self.key_column:
                    self.table[r][c] = tmp_table[r][c] - tmp_table[self.key_row][c]*tmp_table[r][self.key_column]/self.key_value


        self.base_variables[self.key_row-1], self.non_base_variables[self.key_column-1] =  self.non_base_variables[self.key_column-1], self.base_variables[self.key_row-1]
        self.calculate_value()
        print(self.table)

    def phase_two(self):
        while self.check_optimality() == False:
            self.phase_iteration()

    def calculate_table(self):
        tables = []
        if self.phase_one() == False:
            print("Problem sprzeczny")
            tables.append("Problem sprzeczny")
        self.phase_two()

        return tables
