import numpy as np
import logging

def eliminacion_gaussiana_redondeo(A: np.ndarray) -> np.ndarray:
    """Resuelve un sistema de ecuaciones lineales mediante el método de eliminación gaussiana
    con redondeo a dos dígitos y sustitución hacia atrás.

    Args:
        A (np.ndarray): Matriz aumentada del sistema (n x n+1).

    Returns:
        np.ndarray: Vector solución del sistema.
    """
    if not isinstance(A, np.ndarray):
        A = np.array(A, dtype=float)
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n x (n+1)."

    n = A.shape[0]

    # Eliminación Gaussiana sin intercambio de filas
    for i in range(n - 1):
        if A[i, i] == 0:
            raise ValueError("No existe una solución única (matriz singular).")

        # Reducción de filas
        for j in range(i + 1, n):
            m = np.round(A[j, i] / A[i, i], decimals=2)
            A[j, i:] = np.round(A[j, i:] - m * A[i, i:], decimals=2)

        logging.info(f"Paso {i + 1}:\n{A}")

    # Verificar si el sistema tiene solución única
    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe una solución única (matriz singular).")

    # Sustitución hacia atrás
    solucion = np.zeros(n)
    solucion[n - 1] = np.round(A[n - 1, -1] / A[n - 1, n - 1], decimals=2)

    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += A[i, j] * solucion[j]
        solucion[i] = np.round((A[i, -1] - suma) / A[i, i], decimals=2)

    logging.info(f"Solución:\n{solucion}")
    return solucion

# Ejemplo de uso
if __name__ == "__main__":
    Ab = np.array([
        [-1, 4, 1, 8],
        [5/3, 2/3, 2/3, 1],
        [2, 1, 4, 11]
    ])
    solucion = eliminacion_gaussiana_redondeo(Ab)
    print("Solución:", solucion)