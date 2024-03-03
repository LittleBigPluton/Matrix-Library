#!/usr/bin/python3

import math

##############################
####     Class Matrix     ####
##############################

class Matrix:

    # Take class object as a list of matrix's elements
    def __init__(self,elements):
        self.elements = elements
    # Take another matrix's elements and add them by iterating one by one
    # [a1,b1,c1]  [a2,b2,c2]  [a1+a2,b1+b2,c1+c2]
    # [d1,e1,f1]  [d2,e2,f2]  [d1+d2,e1+e2,f1+f2]
    def addition(self,additions):
        try:
            # Create empty list to return it
            result = []
            # Iterate rows if the dimensions of the matrices are more than one
            # This iterates dimensions
            for i in range(len(self.elements)):
                # Create empty list to store additions according to rows
                row = []
                # This iterates elements in a dimension
                for j in range(len(self.elements[0])):
                    # Add two elements with respect to rows one by one
                    row.append(self.elements[i][j]+additions.elements[i][j])
                # Add summations of the elemens in the row
                result.append(row)
            return result
            # If two matrices does not have same dimension, they cannot be added so error raise
        except ValueError:
            print("You cannot add this two matrices because they do not have same dimension.")

    def multiplication(self,multiplications):
        # [a1,b1,c1]    [a2,b2]     [a1*a2 b1*c2 c1*e2]
        # [d1,e1,f1]    [c2,d2]     [d1*b1 e1*d2 f1*f2]
        #               [e2,f2]

        # We will multpily elements of the rows in the matrix 1 with element of the columns of the matrix 2 one by one
        # At the end we will achieve a new matrix
        # [KxM]*[M*N] ==> [KxN]
        try:
            result = []
            # Iterate rows of the first matrix's
            for i in range(len(self.elements)):
                row = []
                # Iterate columns of the second matrix
                for j in range(len(multiplications.elements[0])):
                    multiplication = 0
                    # Iterate coulmn of the first matrix and rows of the second matrix
                    for k in range(len(self.elements[0])):
                        multiplication += self.elements[i][k]*multiplications.elements[k][j]
                    row.append(multiplication)
                result.append(row)
            return result
        # If two matrices does not have same dimension, they cannot be added so error raise
        except ValueError:
            print("You cannot add this two matrices because they do not have same dimension.")

    def vector_multiplication(self,vector):
        try:
            result = []
            # Iterate rows of the matrix
            for i in range(len(self.elements)):
                product = 0
                # Iterate columns of the matrix and vector indexes
                for j in range(len(self.elements[0])):
                    product += self.elements[i][j] * vector[j]
                result.append(product)
            return result
        # If two matrices does not have same dimension, they cannot be added so error raise
        except ValueError:

            print("You cannot add this two matrices because they do not have same dimension.")
    def transpose(self):
        # [a,b,c]           [a,d,g]
        # [d,e,f]   -->     [b,e,h]
        # [g,h,I]           [c,f,I]
        result = []
        for i in range(0,len(self.elements)):
            row = []
            for j in range(0,len(self.elements[0])):
                row.append(self.elements[j][i])
            result.append(row)
        return result

#Define two matrices orderly
M1 = Matrix([[1,2],[3,4]])
M2 = Matrix([[5, 6, 7], [8, 9, 10]])

# For vector multiplication
V = [1, 2, 3]
Summation = M1.addition(M2)
print(Summation)
Multiplication = M1.multiplication(M2)
print(Multiplication)
V_Mult = M1.vector_multiplication(V)
print(V_Mult)
Transpose = M1.transpose()
print(Transpose)