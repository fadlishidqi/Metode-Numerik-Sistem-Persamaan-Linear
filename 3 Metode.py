import numpy as np

# Metode dekomposisi LU Gauss
def luGauss(A, b):
    n = len(A) 
    L = np.eye(n) 
    U = A.copy().astype(float)  

    # Eliminasi Gauss
    for k in range(n-1):
        for i in range(k+1, n):
            faktor = U[i, k] / U[k, k]
            L[i, k] = faktor
            U[i, k:] -= faktor * U[k, k:]
    
    # Solution
    y = np.linalg.solve(L, b.astype(float))  
    x = np.linalg.solve(U, y)
    return x

# Metode dekomposisi Crout
def crout(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

    # Solution
    y = np.linalg.solve(L, b.astype(float))
    x = np.linalg.solve(U, y)
    return x

# Metode dekomposisi Matriks Balikan
def matriksBalikan(A, b):
    A_inv = np.linalg.inv(A) 
    x = np.dot(A_inv, b) 
    return x

# Testing
J = np.array([[4, 5, 6],
              [1, 3, 8],
              [3, 1, 2]])
K = np.array([1, 2, 2])

print("Metode Dekomposisi LU Gauss:")
print(luGauss(J, K))
print("Metode Dekomposisi Crout:")
print(crout(J, K))
print("Metode Matriks Balikan:")
print(matriksBalikan(J, K))