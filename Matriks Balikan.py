import numpy as np

# Metode matriks balikan
def matriksBalikan(A, b):
    A_inv = np.linalg.inv(A) 
    x = np.dot(A_inv, b) 
    return x

# Testing
J = np.array([[4, 5, 6],
              [1, 3, 8],
              [3, 1, 2]])
K = np.array([1, 2, 2])

print("Metode Matriks Balikan:")
print(matriksBalikan(J, K))
