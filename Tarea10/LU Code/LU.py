import numpy as np
import scipy.linalg

A = np.array([
    [1, -1, 2, -1],
    [1, 0, -1, 1],
    [2, 1, 3, -4],
    [0, -1, 1, -1]
], dtype=float)

b1 = np.array([6, 4, -2, 5], dtype=float)  # Primer sistema
b2 = np.array([1, 1, 2, -1], dtype=float)  # Segundo sistema

# LU 
P, L, U = scipy.linalg.lu(A) 

# Resolver Ly = Pb (sustitución progresiva)
y1 = scipy.linalg.solve(L, np.dot(P, b1))
y2 = scipy.linalg.solve(L, np.dot(P, b2))

# Resolver Ux = y (sustitución regresiva)
x1 = scipy.linalg.solve(U, y1)
x2 = scipy.linalg.solve(U, y2)

print("Solución para el primer sistema:")
for i, x in enumerate(x1, start=1):
    print(f"x_{i} = {x:.2f}")

print("\nSolución para el segundo sistema:")
for i, x in enumerate(x2, start=1):
    print(f"x_{i} = {x:.2f}")
