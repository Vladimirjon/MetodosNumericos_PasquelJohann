from scipy.optimize import curve_fit
import numpy as np

x_i = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
y_i = [102.56, 130.11, 113.18, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

def modelo_potencial(x, b, a):
    """
    Modelo potencial de la forma y = b * x^a.
    
    Parámetros:
        x: Array de valores x_i.
        b: Parámetro b del modelo.
        a: Parámetro a del modelo.
    
    Retorna:
        Valores del modelo evaluados en x.
    """
    return b * x**a

def min_cuadrados_potencial(x, y):
    """
    Calcula el ajuste potencial de mínimos cuadrados para el modelo y = b * x^a.
    
    Parámetros:
        x: Lista o array de valores x_i.
        y: Lista o array de valores y_i.
        
    Retorna:
        Resultados formateados con b, a, el error absoluto y el error relativo.
    """
    x = np.array(x)
    y = np.array(y)
    
    # Valores iniciales para b y a
    params_iniciales = [1, 1]
    
    # Ajustar el modelo usando curve_fit
    params_opt, params_cov = curve_fit(modelo_potencial, x, y, p0=params_iniciales)
    b, a = params_opt
    
    # Calcular el modelo ajustado y los errores
    y_pred = modelo_potencial(x, b, a)
    error_absoluto = np.sum(np.abs(y - y_pred))
    error_relativo = np.sum(np.abs((y - y_pred) / y))
    
    return b, a, error_absoluto, error_relativo

b, a, error_absoluto, error_relativo = min_cuadrados_potencial(x_i, y_i)
print(f"b = {b:.4f}, a = {a:.4f}, Error absoluto = {error_absoluto:.4f}, Error relativo = {error_relativo:.4f}")
