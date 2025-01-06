import numpy as np


x_i = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
y_i = [102.56, 130.11, 113.18, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

def min_cuadrados_cubico(x, y):
    """
    Calcula el polinomio de mínimos cuadrados de grado 3 y el error.
    
    Parámetros:
        x: Lista o array de valores x_i.
        y: Lista o array de valores y_i.
        
    Retorna:
        Resultados formateados con a_0, a_1, a_2, a_3, el error absoluto y el error relativo.
    """
    x = np.array(x)
    y = np.array(y)
    
    # Calcular las sumatorias necesarias
    n = len(x)
    sum_x = np.sum(x)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_x5 = np.sum(x**5)
    sum_x6 = np.sum(x**6)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2y = np.sum((x**2) * y)
    sum_x3y = np.sum((x**3) * y)
    
    # Construir el sistema de ecuaciones normales
    A = np.array([
        [n, sum_x, sum_x2, sum_x3],
        [sum_x, sum_x2, sum_x3, sum_x4],
        [sum_x2, sum_x3, sum_x4, sum_x5],
        [sum_x3, sum_x4, sum_x5, sum_x6]
    ])
    B = np.array([sum_y, sum_xy, sum_x2y, sum_x3y])
    
    # Resolver el sistema para encontrar a0, a1, a2, a3
    a0, a1, a2, a3 = np.linalg.solve(A, B)
    
    # Calcular el polinomio ajustado y los errores
    y_pred = a0 + a1 * x + a2 * x**2 + a3 * x**3
    error_absoluto = np.sum(np.abs(y - y_pred))
    error_relativo = np.sum(np.abs((y - y_pred) / y))
    
    # Retornar los coeficientes y los errores
    return f"a_0 = {a0:.4f}, a_1 = {a1:.4f}, a_2 = {a2:.4f}, a_3 = {a3:.4f}, Error absoluto = {error_absoluto:.4f}, Error relativo = {error_relativo:.4f}"



# Llamar a la función
resultado_cubico = min_cuadrados_cubico(x_i, y_i)
resultado_cubico
