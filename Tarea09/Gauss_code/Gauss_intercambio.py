import numpy as np

def eliminacion_gaussiana_con_intercambio(A: np.ndarray) -> np.ndarray:
    """Resuelve un sistema de ecuaciones lineales mediante el método de eliminación gaussiana
    y determina si se necesitan intercambios de fila.

    Args:
        A (np.ndarray): Matriz aumentada del sistema (n x n+1).

    Returns:
        np.ndarray: Vector solución del sistema.
    """
    if not isinstance(A, np.ndarray):
        A = np.array(A, dtype=float)
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n x (n+1)."

    n = A.shape[0]
    intercambios = False

    # Eliminación Gaussiana con detección de intercambios de fila
    for i in range(n - 1):
        # Verificar si se necesita intercambio de filas
        if A[i, i] == 0:
            for k in range(i + 1, n):
                if A[k, i] != 0:
                    A[[i, k]] = A[[k, i]]
                    intercambios = True
                    break
            else:
                raise ValueError("No existe una solución única (matriz singular).")

        # Reducción de filas
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - m * A[i, i:]

    # Verificar si el sistema tiene solución única
    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe una solución única (matriz singular).")

    # Sustitución hacia atrás
    solucion = np.zeros(n)
    solucion[n - 1] = A[n - 1, -1] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += A[i, j] * solucion[j]
        solucion[i] = (A[i, -1] - suma) / A[i, i]

    return solucion, intercambios

Ab = np.array([
    [1, 1, 0, 1, 2],
    [2, 1, -1, 1, 1],
    [4, -1, -2, 2, 0],
    [3, -1, -1, 2, -3]
])
solucion, intercambios = eliminacion_gaussiana_con_intercambio(Ab)
print("Solución:", solucion)
print("Se necesitaron intercambios de fila:", intercambios)