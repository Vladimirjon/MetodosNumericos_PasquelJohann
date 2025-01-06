from scipy.optimize import fsolve
import numpy as np

x_i = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
y_i = [102.56, 130.11, 113.18, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

def sistema_ecuaciones(params, x, y):
    """
    Define el sistema de ecuaciones normales para el modelo y = b * e^(a * x).
    
    Parámetros:
        params: Lista con los valores [b, a] (los parámetros a resolver).
        x: Array de valores x_i.
        y: Array de valores y_i.
    
    Retorna:
        Sistema de ecuaciones evaluado en los parámetros actuales.
    """
    b, a = params
    n = len(x)
    
    # Primera ecuación
    eq1 = np.sum((y - b * np.exp(a * x)) * np.exp(a * x))
    
    # Segunda ecuación
    eq2 = np.sum((y - b * np.exp(a * x)) * x * np.exp(a * x))
    
    return [eq1, eq2]

def min_cuadrados_exponencial(x, y):
    """
    Calcula el ajuste exponencial de mínimos cuadrados para el modelo y = b * e^(a * x).
    
    Parámetros:
        x: Lista o array de valores x_i.
        y: Lista o array de valores y_i.
        
    Retorna:
        Resultados formateados con b, a, el error absoluto y el error relativo.
    """
    # Valores iniciales para b y a
    params_iniciales = [1, 0.1]
    
    # Resolver el sistema de ecuaciones
    b, a = fsolve(sistema_ecuaciones, params_iniciales, args=(x, y))
    
    # Calcular el modelo ajustado y los errores
    y_pred = b * np.exp(a * x)
    error_absoluto = np.sum(np.abs(y - y_pred))
    error_relativo = np.sum(np.abs((y - y_pred) / y))
    
    return b, a, error_absoluto, error_relativo