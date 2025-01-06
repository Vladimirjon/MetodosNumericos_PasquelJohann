import numpy as np


x_i = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
y_i = [102.56, 130.11, 113.18, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

def min_cuadrados_cuadratico(x, y):
    """
    Calcula el polinomio de mínimos cuadrados de grado 2 y proporciona resultados con etiquetas claras.
    
    Parámetros:
        x: Lista o array de valores x_i.
        y: Lista o array de valores y_i.
        
    Retorna:
        Resultados formateados con a_0, a_1, a_2, el error absoluto y el error relativo.
    """

    x = np.array(x)
    y = np.array(y)
    
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_xy = np.sum(x * y)
    sum_x2y = np.sum(x**2 * y)
    
    # Construir las matrices del sistema de ecuaciones normales
    A = np.array([
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ])
    B = np.array([sum_y, sum_xy, sum_x2y])
    
    # Resolver el sistema para encontrar a0, a1, a2
    a0, a1, a2 = np.linalg.solve(A, B)
    
    # Calcular el polinomio ajustado y los errores
    y_pred = a0 + a1 * x + a2 * x**2
    error_absoluto = np.sum(np.abs(y - y_pred))
    error_relativo = np.sum(np.abs((y - y_pred) / y))
    
    return f"a_0 = {a0:.4f}, a_1 = {a1:.4f}, a_2 = {a2:.4f}, Error absoluto = {error_absoluto:.4f}, Error relativo = {error_relativo:.4f}"


resultado_cuadratico = min_cuadrados_cuadratico(x_i, y_i)
print(resultado_cuadratico)