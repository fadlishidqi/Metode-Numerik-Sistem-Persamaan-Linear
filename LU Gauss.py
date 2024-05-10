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

# Testing
J = np.array([[4, 5, 6],
              [1, 3, 8],
              [3, 1, 2]])
K = np.array([1, 2, 2])

print("Metode Dekomposisi LU Gauss:")
print(luGauss(J, K))