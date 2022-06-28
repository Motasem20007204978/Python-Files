# importing Numpy package
import numpy as np

n_array = np.array([[7,6], [4,4]])# creating a 2X2 Numpy matrix
base = 27#to be used in mod

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print(f"\nDeterminant of given matrix: {int(det)}")
print(f"det % {base} is {int(det)%base}")
