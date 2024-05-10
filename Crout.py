import numpy as np

# Metode dekomposisi Crout
def crout(A, b):
    n = len(A) 
    L = np.zeros((n, n)) 
    U = np.zeros((n, n)) 

    for i in range(n):
        L[i, i] = 1
    for j in range(n):
        for i in range(j, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(j))
    for j in range(n):
        for i in range(j+1, n):
            L[i, j] = (A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))) / U[j, j]
    
    # Solution
    y = np.linalg.solve(L, b.astype(float))
    x = np.linalg.solve(U, y)
    return x

# Testing
J = np.array([[4, 5, 6],
              [1, 3, 8],
              [3, 1, 2]])
K = np.array([1, 2, 2])

print("Metode Dekomposisi Crout:")
print(crout(J, K))
