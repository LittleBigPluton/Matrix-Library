#!/usr/bin/python3
import matrix_operations as MO
#Define two matrices orderly
M1 = MO.Matrix([[1,2],[3,4]])
M2 = MO.Matrix([[5, 6, 7], [8, 9, 10]])

# For vector multiplication
V = [1, 2, 3]
Summation = M1.Addition(M2)
print(Summation)
Multiplication = M1.MatrixMultiplication(M2)
print(Multiplication)
V_Mult = M1.VectorMultiplication(V)
print(V_Mult)
Transpose = M1.Transpose()
print(Transpose)
print(M1.ScalarMultiplication(3))
