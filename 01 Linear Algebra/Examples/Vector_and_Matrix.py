import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from VectorClass import Vector
from MatrixClass import Matrix

# Examples for the Vectors Class

v1 = Vector([1, 2, 3, 4, 5])

print(f"Input vector v1: {v1}")
print(f"Input vector size = {v1.size()}")
print(f"Input vector scaled by 3 = {v1.scale(3)}")
print(f"Input vector magnitude = {v1.norm()}")
print(f"Input vector normalized = {v1.normalize().data}")

v2 = Vector([6, 7, 8, 9, 0])
print(f"Second Input vector v2: {v2}")
print(f"v1 + v2 = {v1.add(v2).data}")
print(f"v1 - v2 = {v1.subtract(v2).data}")
print(f"v1 dot v2 = {v1.dot(v2)}")
print(f"Distance between v1 & v2 = {v1.distance(v2)}")

# Testing shorthand functions
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"3 * v1 = {3 * v1}")

# --------------------------------------------------

# Testing Matrix Class

M1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

M2 = Matrix([
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]])

print(f"Input Matrix M1 = {M1.data}")
print(f"Input Matrix Shape = {M1.shape()}")
print(f"Input Matrix Row number = {M1.rows()}")
print(f"Input Matrix Col number = {M1.cols()}")
print(f"Input Matrix 3nd row = {M1.row(2)}")
print(f"Input Matrix 3nd col = {M1.col(2)}")
print(f"Input Matrix transpose = {M1.transpose()}")
print(f"Second Matrix M2 = {M2.data}")
print(f"Matrix Product M1 * M2 = {M1.multiply(M2)}")




