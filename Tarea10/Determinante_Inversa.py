import numpy as np

def calcular_determinante_inversa(matriz):
    # Calcular el determinante de la matriz
    determinante = np.linalg.det(matriz)
    
    if determinante == 0:
        return determinante, None + "Matriz no tiene inversa porque determinante es 0."
    else:
        # Calcular la inversa de la matriz
        inversa = np.linalg.inv(matriz)
        return determinante, inversa

# Ejemplo de uso
if __name__ == "__main__":
    matriz = np.array([[1, 2], [3, 4]])
    determinante, inversa = calcular_determinante_inversa(matriz)
    
    print(f"Determinante: {determinante}")
    if inversa is not None:
        print("Inversa:")
        print(inversa)
    else:
        print("La matriz no tiene inversa porque su determinante es 0.")