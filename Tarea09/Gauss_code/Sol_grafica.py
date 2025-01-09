from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def graficar_sistema_general(coeficientes, independientes):
    """
    Grafica un sistema de ecuaciones lineales en 2D, 3D o resuelve algebraicamente para dimensiones mayores.
    
    Args:
        coeficientes: Lista de listas con los coeficientes de las ecuaciones.
        independientes: Lista de los términos independientes.
    """
    num_ecuaciones = len(coeficientes)
    num_incognitas = len(coeficientes[0])
    
    # Caso 2 incógnitas (2D)
    if num_incognitas == 2:
        x = np.linspace(-10, 10, 400)
        plt.figure(figsize=(8, 6))
        
        for i, (a, b) in enumerate(coeficientes):
            y = (independientes[i] - a * x) / b
            plt.plot(x, y, label=f'Ecuación {i + 1}: {a}x + {b}y = {independientes[i]}')
        
        try:
            A = np.array(coeficientes)
            B = np.array(independientes)
            solucion = np.linalg.solve(A, B)
            plt.scatter(solucion[0], solucion[1], color='red', label=f'Solución: {solucion}')
        except np.linalg.LinAlgError:
            plt.title("No hay solución única (sistema dependiente o incompatible)")
        
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Sistema de ecuaciones en 2D')
        plt.show()
    
    # Caso 3 incógnitas (3D)
    elif num_incognitas == 3:
        x = np.linspace(-10, 10, 20)
        y = np.linspace(-10, 10, 20)
        X, Y = np.meshgrid(x, y)
        
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        for i, (a, b, c) in enumerate(coeficientes):
            Z = (independientes[i] - a * X - b * Y) / c
            ax.plot_surface(X, Y, Z, alpha=0.5, label=f'Ecuación {i + 1}')
        
        try:
            A = np.array(coeficientes)
            B = np.array(independientes)
            solucion = np.linalg.solve(A, B)
            ax.scatter(solucion[0], solucion[1], solucion[2], color='red', label=f'Solución: {solucion}')
        except np.linalg.LinAlgError:
            ax.set_title("No hay solución única (sistema dependiente o incompatible)")
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.title('Sistema de ecuaciones en 3D')
        plt.legend()
        plt.show()
    
    # Caso más de 3 incógnitas
    else:
        try:
            A = np.array(coeficientes)
            B = np.array(independientes)
            solucion = np.linalg.solve(A, B)
            print(f"El sistema tiene solución única: {solucion}")
        except np.linalg.LinAlgError:
            print("No hay solución única para este sistema (puede ser dependiente o incompatible).")