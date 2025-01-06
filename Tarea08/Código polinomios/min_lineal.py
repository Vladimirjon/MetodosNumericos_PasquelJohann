import numpy as np
import matplotlib.pyplot as plt


def min_cuadrados_lineal(x, y):
    """
    Calcula el polinomio de mínimos cuadrados de grado 1 y proporciona resultados con etiquetas claras.
    
    Parámetros:
        x: Lista o array de valores x_i.
        y: Lista o array de valores y_i.
        
    Retorna:
        Resultados formateados con a_0, a_1, el error absoluto y el error relativo.
    """
    
    # Convertir a arrays de NumPy para operaciones vectorizadas
    x = np.array(x)
    y = np.array(y)
    
    # Calcular las sumatorias
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)
    
    # Resolver el sistema de ecuaciones normales
    A = np.array([[n, sum_x], [sum_x, sum_x2]])
    B = np.array([sum_y, sum_xy])
    a0, a1 = np.linalg.solve(A, B)
    
    # Calcular el polinomio y los errores
    y_pred = a0 + a1 * x
    error_absoluto = np.sum(np.abs(y - y_pred))
    error_relativo = np.sum(np.abs((y - y_pred) / y))
    
    # Retornar los valores de a0, a1, el error absoluto y el error relativo
    return f"a_0 = {a0}, a_1 = {a1}, Error absoluto = {error_absoluto}, Error relativo = {error_relativo}"

# Definición de x_i y y_i fuera de la función
x_i = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
y_i = [102.56, 130.11, 113.18, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

# Ejemplo de uso
resultado = min_cuadrados_lineal(x_i, y_i)
print(resultado)


# Obtener los coeficientes a_0 y a_1 de la función
a0, a1 = [float(value.split('=')[1]) for value in resultado.split(',')[:2]]

# Generar valores de x para la línea de regresión
x_line = np.linspace(min(x_i), max(x_i), 100)
y_line = a0 + a1 * x_line

# Graficar los puntos originales y la línea de regresión
plt.scatter(x_i, y_i, color='blue', label='Datos originales')
plt.plot(x_line, y_line, color='red', label='Línea de mínimos cuadrados')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste por mínimos cuadrados lineal')
plt.legend()
plt.show()