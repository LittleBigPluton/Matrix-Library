##############################
####   Import Libraries   ####
##############################

import math

##############################
####     Class Matrix     ####
##############################

class Matrix:

    # Take class object as a list of matrix's elements
    def __init__(self,init_matrix):
        self.elements = init_matrix
        self.rows = len(self.elements)
        self.columns = len(self.elements[0])
    # Take another matrix's elements and add them by iterating one by one
    # [a1,b1,c1]  [a2,b2,c2]  [a1+a2,b1+b2,c1+c2]
    # [d1,e1,f1]  [d2,e2,f2]  [d1+d2,e1+e2,f1+f2]
    def Addition(self,addition_matrix):
        try:
            # Create empty list to return it
            result = []
            # Iterate rows if the dimensions of the matrices are more than one
            # This iterates dimensions
            for i in range(self.rows):
                # Create empty list to store additions according to rows
                row = []
                # This iterates elements in a dimension
                for j in range(self.columns):
                    # Add two elements with respect to rows one by one
                    row.append(self.elements[i][j]+addition_matrix.elements[i][j])
                # Add summations of the elemens in the row
                result.append(row)
            return result
            # If two matrices does not have same dimension, they cannot be added so error raise
        except ValueError:
            print("You cannot add this two matrices because they do not have same dimension.")

    def MatrixMultiplication(self,multiplication_matrix):
        # [a1,b1,c1]    [a2,b2]     [a1*a2 b1*c2 c1*e2]
        # [d1,e1,f1]    [c2,d2]     [d1*b1 e1*d2 f1*f2]
        #               [e2,f2]

        # We will multpily elements of the rows in the matrix 1 with element of the columns of the matrix 2 one by one
        # At the end we will achieve a new matrix
        # [KxM]*[M*N] ==> [KxN]
        try:
            result = []
            # Iterate rows of the first matrix's
            for i in range(self.rows):
                row = []
                # Iterate columns of the second matrix
                for j in range(len(multiplication_matrix.elements[0])):
                    multiplication = 0
                    # Iterate coulmn of the first matrix and rows of the second matrix
                    for k in range(self.columns):
                        multiplication += self.elements[i][k]*multiplication_matrix.elements[k][j]
                    row.append(multiplication)
                result.append(row)
            return result
        # If two matrices does not have same dimension, they cannot be added so error raise
        except ValueError:
            print("You cannot add this two matrices because they do not have same dimension.")

    def ScalarMultiplication(self,constant):
        try:
            # Iterate all elements through the list/matrix and multiply with entered constant
            # Return a new list, conserve the original matrix
            return [[element*constant for element in rows] for rows in self.elements]
        except TypeError:
            print("All elements in the matrix must be numbers.")
        except ValueError:
            print("Invalid value encountered during multiplication.")


    def VectorMultiplication(self,vector):
        try:
            result = []
            # Iterate rows of the matrix
            for i in range(self.rows):
                product = 0
                # Iterate columns of the matrix and vector indexes
                for j in range(self.columns):
                    product += self.elements[i][j] * vector[j]
                result.append(product)
            return result
        # If two matrices does not have same dimension, they cannot be added so error raise
        except ValueError:

            print("You cannot add this two matrices because they do not have same dimension.")
    def Transpose(self):
        # [a,b,c]           [a,d,g]
        # [d,e,f]   -->     [b,e,h]
        # [g,h,I]           [c,f,I]
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self.elements[j][i])
            result.append(row)
        return result
